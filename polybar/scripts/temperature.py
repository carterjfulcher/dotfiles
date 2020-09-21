#!/usr/bin/python3

import os 

data = os.popen('sensors').readlines()
print(data[15].replace('(high = +100.0°C, crit = +100.0°C)', '').replace('Package id 0:  +', ''))



