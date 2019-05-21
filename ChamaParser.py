#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
        
path = ('teste.cmd')
#print (path)
#print(os.startfile(path))

# print(os.getpid())
r = subprocess.call(['teste.cmd', "-h"])
#print(r)
  