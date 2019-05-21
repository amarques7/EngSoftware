#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

def doxygen_Ex(localpath):
        
  #path = (localpath + 'Excut_Dox.cmd')
  # print ("locapath: ", localpath)
    
   # print(os.startfile(path))

   # print(os.getpid())
    #r = subprocess.call([localpath + "Excut_Dox.cmd", "-h"])
   r = subprocess.call(["Doxygen", localpath + "/Doxyfile"])
   print('r: ',r)
   #exit(0)
   return r