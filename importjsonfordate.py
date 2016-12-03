import urllib.request
import argparse
import logging
import csv
import time
import json

#if new user - prompt with firstdate
sensorname = raw_input 'Enter your sensor name:'
dweetkey = raw_input 'Enter your read/write dweet lock key:'
modelingfile = raw_input 'Enter your the name of the modeling file to create:'

firstdate = raw_input 'Enter the date (ie 2016-11-25):'
urllib.request.urlretrieve('https://dweet.io/get/stored/dweets/for/'+sensorname+'?key='+dweetkey+'&date='+date, modelingfile+'.json')
time.sleep(3)

#if returning user - prompt with appenddate
appenddate = raw_input 'Enter the date to add to your data set (ie 2016-11-25):'
sensorname+_web = urllib.request.urlopen('https://dweet.io/get/stored/dweets/for/'+sensorname+'?key='+dweetkey+'&date='+appenddate);
with open(modelingfile+'.json', 'r') as sensorname+_file:
  sensorname+_file.write(sensorname+_web.read())
  time.sleep(1)

try:
fileopen = open(modelingfile.json, 'r')
except:
  print 'file cannot be opened'
  exit()
  
#get average temp for day in Miss America
# Use the file name mbox-short.txt as the file name
total=0
count=0
for line in fileopen:
    if not line.startswith("TemperatureSensor") : continue
    pos = line.find("TemperatureSensor:")
    num =  float(line[pos+1:pos+18].lstrip())
    total += num
    count = count + 1
    
avgTemp = total/count
print 'Average Temp:',avg
