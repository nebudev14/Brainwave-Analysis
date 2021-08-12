from telnetlib import Telnet
import sys
import json

tn = Telnet('localhost', 13854)
tn.write('{"enableRawOutput": true, "format": "Json"}'.encode("utf-8"))

while True:
    line=tn.read_until('\r'.encode("utf-8"))
    dict=json.loads(str(line.decode("utf-8")))
    if 'eSense' in dict:
        print(dict['eSense'])
    