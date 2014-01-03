#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import glob
import tkMessageBox


for param in sys.argv:
    tkMessageBox.showinfo("Say Hello", param)


#lista = glob.glob('*est*')
#print lista


