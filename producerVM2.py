#
#
# Author: Aadarsh and Ashwin
# Send energy data to consumer
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

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
# Connects to VM2

producer = KafkaProducer(bootstrap_servers="129.114.26.3:30003", api_version=(0, 1, 0), acks=0)
df = pd.read_csv('energy-sorted1M-PVM1-2.csv', header=None)

for i in range(0, len(df), 1000):
    producer.send("utilizations2", df[i:i+1000].to_json(orient="split").encode('utf-8'))
    producer.flush()
    # sleep a second
    time.sleep(1)

# we are done
producer.close()


