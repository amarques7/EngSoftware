#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def deletatodos(dir_arq):
   
      test = os.listdir(dir_arq)
      for item in test:
        if  item.endswith(".dot"):
              os.unlink(os.path.join(dir_arq, item))