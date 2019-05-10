#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

def doxygen_Ex():
        
    path = ('Excut_Dox.cmd')
    #print (path)
   # print(os.startfile(path))

   # print(os.getpid())
    r = subprocess.call(["Excut_Dox.cmd", "-h"])
    #print(r)
    return r