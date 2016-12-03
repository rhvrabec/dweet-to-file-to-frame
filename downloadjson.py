import sys
import urllib.request
import argparse
import logging
import csv
import time
import json
import pandas

sensorname = input("Enter your sensor name:")
dweetkey = input("Enter your read/write dweet lock key:")
firstdate = input("Enter the date (format must be: yyyy-mm-dd):")
modelingfile = sensorname+firstdate
urllib.request.urlretrieve('https://dweet.io/get/stored/dweets/for/'+sensorname+'?key='+dweetkey+'&date='+firstdate, modelingfile+'.json')
time.sleep(3)
