from flask_restful import Api, Resource, reqparse
from tensorflow.keras.datasets import mnist

from kafka import KafkaProducer
import couchdb

import time
import random
import string
import json
import numpy
import pandas as pd

class HelloApiHandler(Resource):
  def get(self):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))
    x_test = x_test.astype('float32')
    x_test /= 255
    send_array = x_test[0:10]

    print(send_array[0])

    output = predict(send_array[0])

    return {
      'resultStatus': 'SUCCESS',
      'message': f"{output}"
    }

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('image', type=str)

    args = parser.parse_args()

    # get data
    image_str = args['image']
    image_str = image_str[1:-1]

    # preprocessing
    img = image_str.split(",")
    img = numpy.array(img)
    img = img.reshape((28, 28, 1))
    img = img.astype('float32')
    img /= 255

    ret_msg = predict(img)

    return {"status": "Success", "prediction": ret_msg}


def predict(img):
    randValue = random.randint(1,3)
    producer = KafkaProducer(bootstrap_servers="129.114.26.3:3000{}".format(randValue), api_version=(0, 1, 0), acks=0)

    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
    producer.send("utilizations2", json.dumps({key : img.tolist()}).encode('utf-8'))
    producer.flush()
    # sleep a second
    time.sleep(1)
    # we are done
    producer.close()

    #Build couchDB server object
    couch = couchdb.Server("http://admin:cloud123@129.114.26.3:30006")
    db = couch['pred-dig']
    rows = db.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    df = pd.DataFrame(data)


    col = df[key].dropna()
    answer = col[list(col.keys())[0]]
    print('Key: {}, Output: {}'.format(key, answer))

    return answer
