import urllib.request
import argparse
import logging
import csv
import time
import json

urllib.request.urlretrieve('https://dweet.io/get/stored/dweets/for/gabysensortag?key=2o4CTz73ZBbrjxS5zE8tU5&date=2016-11-03', 'gabysensortag.json')
time.sleep(3)

open(.json, 'r')
