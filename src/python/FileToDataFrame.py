# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:31:37 2021

@author: vanch
"""

import pandas as pd
import re
import shutil
import os

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
        shutil.copy(self.fileName, os.path.splitext(self.fileName)[0]+"_temp.txt")
        
        output = open(self.tempFileName, "w", encoding="utf8")
        input = open(self.fileName, encoding="utf8" , errors='replace')
        
        for line in input:
            output.write(self.replacenth(re.sub(r'-', r',', line, 1), r':' , r',' , 2))
        
        input.close()
        output.close()
        
    def __prepareDataFrame(self):
        self.Df =  pd.read_csv(self.tempFileName, sep=',', usecols=range(4),
                 lineterminator='\n',names=["Date", "Time", "Name", "Msg"])
        
                