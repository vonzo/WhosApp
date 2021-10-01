# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:54:46 2021

@author: vanch
"""

import argparse
import FileToDataFrame as ftd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='')
args = parser.parse_args()

print (args.filename)

#df = ftd.FileToDataFrame(args.filename)
df = ftd.FileToDataFrame("../../samples/Gunners.txt")

print(df.Df.Name.unique())
