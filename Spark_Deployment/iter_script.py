# Script to run spark at 20 iterations
import time
import os
import subprocess
import pandas as pd


conf_array = ["_100_10", "_50_5", "_10_2"]
for conf in conf_array:
    time_array = []
    for i in range(20):
        t = time.time()
        spark_submit_str= "spark-3.2.0-bin-hadoop3.2/bin/spark-submit --master spark://spark-master-svc:7077 --properties-file spark-3.2.0-bin-hadoop3.2/conf/spark-driver{}.conf energy-counter.py".format(conf)
        process=subprocess.Popen(spark_submit_str,stdout=subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        stdout,stderr = process.communicate()
        if process.returncode !=0:  
            print(stderr)
        print(stdout)
        time_array.append((time.time() - t))
        
    print('\n\n\n\nTIME_OUTPUT:\n')
    print(*time_array, sep = "\n")
    df = pd.DataFrame(time_array)
    df.to_csv('time{}.csv'.format(conf), index=None, header=None)