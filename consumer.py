#
#
# Author: Aadarsh and Ashwin
#

import os  # need this for popen
import time  # for sleep
from kafka import KafkaConsumer  # consumer of events
import couchdb  # python couchdb api
from datetime import datetime
import json
import sys

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer(bootstrap_servers="129.114.26.3:30002")

# subscribe to topic
consumer.subscribe(topics=["utilizations1", "utilizations2"])
print('Subscribed to topics')

# # #Build couchDB server object
couch = couchdb.Server("http://admin:cloud123@129.114.26.3:30006")

# See if DB exists, if not, build DB
dbname = "energy-set"

if dbname in couch:
    db = couch[dbname]
else:
    db = couch.create(dbname)
print('Connected to CouchDB server and database')

# we keep reading and printing
for msg in consumer:
    jsonObject = json.loads(msg.value)
    db.save({'data': jsonObject['data']})

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close()
