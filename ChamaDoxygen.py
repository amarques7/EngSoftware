    #!/usr/bin/env python
# -*- coding: utf-8 -*-
import re 
import csv
import os
import glob
import time
import subprocess

def doxygenEx()
    
    path = ('Excut_Dox.cmd')
    print (path)
    print(os.startfile(path))

    print(os.getpid())
    r = subprocess.call(["Excut_Dox.cmd", "-h"])
    print(r)
return (r))