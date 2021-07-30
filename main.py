# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:41:50 2021

@author: Ian
"""
import os

master = open("settings.txt", "r")


def loadSettings():
    
    
def greeting():
    print("Hello,", os.getlogin(), "Where is the data you would like to process?")
    navigation()

def navigation():
    print("Current directory:", os.getcwd())
    print("Contains:", os.listdir(os.getcwd()))

    
    
def getData():
    print()
    

    
greeting()

