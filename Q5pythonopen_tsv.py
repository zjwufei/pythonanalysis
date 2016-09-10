# -*- coding: utf-8 -*-
"""
Spyder Editor

Open tsv file in python.
"""
import csv 

with open('/Users/Yan/Desktop/tsv.tsv','r') as tsv:
    datatsv = [line.strip().split('\t') for line in tsv]

targetTSV=datatsv[1048576]