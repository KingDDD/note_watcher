#!/usr/bin/env python
#King D

import csv

PATH = '/home/d/pose.csv'

file = open(PATH)
reader = csv.reader(file)
header = next(reader)

data = []
for row in reader:
    print(row[2])
    timestamps = int(row[2])
    posX = float(row[3])
    posY = float(row[4])
    posZ = float(row[5])
    quatW = float(row[6])
    quatX = float(row[7])
    quatY = float(row[8])
    quatZ = float(row[9])

print(posX[2])
    
