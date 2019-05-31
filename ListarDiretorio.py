#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def listardiretorio(path,i):
    subdir = list() 

    for r, d, f in os.walk(path):
        for folder in d:
          subdir.append(os.path.join(r,folder))     

    return(subdir[i])        
  