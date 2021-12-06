#
#
# Author:
#
#
import json
import os  # need this for popen
import time  # for sleep
from kafka import KafkaProducer  # producer of events
from datetime import datetime
import json
import requests
from bson import json_util
import sys
import pandas as pd
import tensorflow as tf
import numpy as np
import random
import string

from tensorflow.keras.datasets import mnist
from keras.utils import np_utils
import couchdb  # python couchdb api

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
# Connects to VM2
nb_classes = 10
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# prepare images for Conv2D layer
# reshape dataset to have a single channel
#x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# Convert data to float
# This is a keras specific step
#x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# scale the pixel values from [0,255] to [0,1]
#x_train /= 255
x_test /= 255


# Select five images to send and get results
send_array = x_test[0:10]
output_results = y_test[0:10]

producer = KafkaProducer(bootstrap_servers="129.114.26.3:30001", api_version=(0, 1, 0), acks=0)
key_array = []

for i in range(len(send_array)):
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
    key_array.append(key)
    # print('Key: {}, Value: {}'.format(key, output_results[i]))
    producer.send("utilizations2", json.dumps({key : send_array[i].tolist()}).encode('utf-8'))
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

for i in range(len(key_array)):
    col = df[key_array[i]].dropna()
    print('Key: {}, Output: {}, Actual: {}'.format(key_array[i],
                col[list(col.keys())[0]], output_results[i]))
