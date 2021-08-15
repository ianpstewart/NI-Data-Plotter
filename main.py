# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:41:50 2021

@author: Ian
"""
import os
import sys

master = open("settings.txt", "r")


def loadSettings():
    print()
    
    
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
            print(openFile)
    else:
        print("failed")
        sys.exit()
     
        
    if openFile == "Y" or openFile == "y":
        getData(os.getcwd() + "/" + filesContained[changeTo - 1])
    else:
        navigation()
    
        
    
    
        

    
    
def getData(fileName):
    print("you did idt")
    sys.exit()
    

    
greeting()

