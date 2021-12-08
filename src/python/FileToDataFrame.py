# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:31:37 2021

@author: vanch
"""

import pandas as pd
import re
import shutil
import os
from collections import Counter

class FileToDataFrame:
    def __init__(self, fileName):
        if(isinstance(fileName, str)):
            self.fileName = fileName
            self.tempFileName = os.path.splitext(self.fileName)[0]+"_temp.txt"
        else:
            print("Invalid input")
        self.cnt = 0
        self.__prepareFile()
        self.__prepareDataFrame()
        
        
    def replacenth(self, string, sub, wanted, n):
        try:
            where = [m.start() for m in re.finditer(sub, string)][n-1]
            before = string[:where]
            after = string[where:]
            after = after.replace(sub, wanted, 1)
            newString = before + after
        except:
            self.cnt = self.cnt +1
            #print(string + str(self.cnt))
            newString = ''
        return newString
            
    def __prepareFile(self):
        #shutil.copy(self.fileName, os.path.splitext(self.fileName)[0]+"_temp.txt")
        datetime_pattern = '\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s[AP]M'

        with open(self.fileName, "r", encoding="utf8") as out_lines:
            lines = out_lines.readlines()
            
        with open(self.tempFileName, "w", encoding="utf8" , errors='replace') as in_lines:
            for line in lines:
                has_datetime = bool(re.match(datetime_pattern, line))
                if(has_datetime):
                    in_lines.write('\n')
                    
                    in_lines.write(self.replacenth(re.sub(r'-', r',', re.sub(r',',r'',line,1), 1), r':' , r',' , 2).strip('\n'))
                else:
                    in_lines.write(line.strip('\n'))
    
        
    def __prepareDataFrame(self):
        self.Df =  pd.read_csv(self.tempFileName, sep=',', usecols=range(3),
                 lineterminator='\n',names=["Date", "Name", "Msg"]).dropna()
        #Set Date time format
        self.Df['Date'] = pd.to_datetime(self.Df['Date'])
           
        
                