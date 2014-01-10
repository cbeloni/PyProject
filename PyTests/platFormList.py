#!/usr/bin/python

# -*- coding: utf-8 -*-

import os, sys, platform, traceback

def obtem_arquivos():
    text_file = open("logFile.txt", "w")
    n = 0
    for param in sys.argv:
        text_file.write(param + "\n")
        if n == 1:
            d = os.listdir(param)
            text_file.write(d)
            text_file.write("gravou dentro if "+ str(n) + "\n" )
        n +=1
    text_file.close() 

try:
    obtem_arquivos()
except:
    erro_file = open("logErro.txt", "w")
    erro_file.write(sys.exc_info())
    erro_file.close()

    print (sys.exc_info())