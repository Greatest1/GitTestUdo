#32 sensor dummy dataset with 16 floats between '0 & 1' each; 

import random
from datetime import datetime

user_date = datetime.now()
print user_date

raw_data=([[random.random() for sensor in range(16)] for cluster in range(32)])
print raw_data

# Creating error 'err'

for error in range(random.randint(1,10)):
    err_cluster_pos=random.randint(1,32)
    err_sensor_pos=random.randint(1,16)
    raw_data[err_cluster_pos-1][err_sensor_pos-1]='err'
    print raw_data



# Creating a copy of corrupted dataset

import csv


file = "Corrupted_Data_File.csv"
with open(file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(raw_data)):
        test=raw_data[i]
        #print(test)
        writer.writerow(test)

import logging
import logging.config

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.error('is when this event was logged.')
