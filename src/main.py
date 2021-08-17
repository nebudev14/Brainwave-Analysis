from telnetlib import Telnet
import sys
import json
import time
import csv

tn = Telnet('localhost', 13854)
tn.write('{"enableRawOutput": true, "format": "Json"}'.encode("utf-8"))

avg_attention = 0
avg_meditation = 0
total_attention = 0
total_meditation = 0
iter = 0

while True:
    line=tn.read_until('\r'.encode("utf-8"))
    dict=json.loads(str(line.decode("utf-8")))
    if 'eSense' in dict:
        iter += 1
        total_attention += dict['eSense']['attention']
        avg_attention = total_attention/iter
        total_meditation += dict['eSense']['meditation']
        avg_meditation = total_meditation/iter
        print("Average attention level: " + str(avg_attention))
        print("Current attention level: " + str(dict['eSense']['attention']))
        print("Average meditation level: " + str(avg_meditation))
        print("Current meditation level: " + str(dict['eSense']['meditation']))
        print("-------")

