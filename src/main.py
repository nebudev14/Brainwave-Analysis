from telnetlib import Telnet
import sys
import json
import time
import random
import csv

tn = Telnet('localhost', 13854)
tn.write('{"enableRawOutput": true, "format": "Json"}'.encode("utf-8"))

avg_attention = 0
total_attention = 0
iter = 0

while True:
    line=tn.read_until('\r'.encode("utf-8"))
    dict=json.loads(str(line.decode("utf-8")))
    if 'eSense' in dict:
        iter += 1
        total_attention += dict['eSense']['attention']
        avg_attention = total_attention/iter
        print(avg_attention)
