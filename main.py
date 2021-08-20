# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:41:50 2021

@author: Ian
"""
import os
import sys

master = open("settings.txt", "r")



class instrument:
    def __init__(self, name, yUnit, xUnit, samples):
        self.name = name
        self.yUnit = yUnit
        self.xUnit = xUnit
        self.samples = samples
        
        xVals = []
        yVals = []
        
    
    def factor(self, scale):
        for item in self.yVals:
            item = item * scale
        
    def addX(self, xVal):
        self.xVals.append(xVal)
        
    def addY(self, yVal):
        self.yVals.append(yVal)
        

def processData(data):
    for item in data:
        print(item)



def getData(fileName):
    dataFile = open(fileName, "r")
    data = dataFile.readlines()
    
    xUnits = []
    yUnits = []
    for lineNum, line in enumerate(data):
        listLine = line.split()
        if "Y_Unit_Label" in listLine:
            yUnits.extend(listLine)
        elif "X_Dimension" in listLine:
            xUnits.extend(listLine)
        elif "X_Value" in listLine:
            processData(data[lineNum:])
                    
    print(xUnits)
        
       
    

    
def greeting():
    print("Hello,", os.getlogin(), "where is the data you would like to process?")
    navigation()
    
    
def navigation():
    print("Current directory:", os.getcwd())
    filesContained = os.listdir(os.getcwd())
    for place, thing in enumerate(filesContained, start = 1):
        print(place, thing)
        
    changeTo = int(input("Enter Number or 0 for back: "))
    if changeTo == 0 or "":
        os.chdir('../')
        navigation()
    elif changeTo > len(filesContained):
        print("failed")
        sys.exit()
    elif int(changeTo):
        if(os.path.isdir(os.getcwd() + "/" + filesContained[changeTo - 1])):
            os.chdir(os.getcwd() + "/" + filesContained[changeTo - 1])
            navigation()
        else:
            prompt = "Y/N would you like to open - " + os.getcwd() + "/" + filesContained[changeTo - 1] + " - "
            openFile = input(prompt)
            if openFile == "Y" or openFile == "y":
                getData(os.getcwd() + "/" + filesContained[changeTo - 1])
            else:
                navigation()
            
    else:
        print("failed")
        sys.exit()
     
 
    

    
    
            
    

    
greeting()

