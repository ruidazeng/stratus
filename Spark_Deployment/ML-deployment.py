from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical

from elephas.spark_model import SparkModel
from elephas.utils.rdd_utils import to_simple_rdd

from pyspark import SparkContext, SparkConf
from keras.utils import np_utils
import time
import numpy as np

# Define basic parameters
batch_size = 64
nb_classes = 10
epochs = 10

# Create Spark context
master_url = "spark://spark-master-svc:7077"
conf = SparkConf().setAppName('Mnist_Spark_MLP').setMaster(master_url)\
    .set("spark.driver.host", "spark-driver-svc").set("spark.driver.bindAddress", "spark-driver-host")\
    .set("spark.driver.port", "7076").set("spark.blockManager.port", "7079")
sc = SparkContext(conf=conf)

# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# prepare images for Conv2D layer
# reshape dataset to have a single channel
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# Convert data to float
# This is a keras specific step
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# scale the pixel values from [0,255] to [0,1]
x_train /= 255
x_test /= 255

# Convert class vectors to binary class matrices
y_train = np_utils.to_categorical(y_train, nb_classes)
y_test = np_utils.to_categorical(y_test, nb_classes)

#Create model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(nb_classes, activation='softmax'))
model.summary() 

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Build RDD from numpy features and labels
rdd = to_simple_rdd(sc, x_train, y_train)

# Initialize SparkModel from tensorflow.keras model and Spark context
spark_model = SparkModel(model, frequency='epoch', num_workers=5, mode='synchronous')

# Train Spark model
start_time = time.time()
spark_model.fit(rdd, epochs=epochs, batch_size=batch_size, verbose=4, validation_split=0.1)
end_time = time.time()
# Evaluate Spark model by evaluating the underlying model
score = spark_model.evaluate(x_test, y_test, verbose=2)
print('Test accuracy:', score[1])

np.savetxt('results.txt', [end_time-start_time, score[1]], fmt="%f")
spark_model.save('mnist_model')