#!/usr/bin/env python
# -*- coding: utf-8 -*-import os
import os 

def delete(dir_arq):
  test = os.listdir(dir_arq)
  for item in test:
    if not item.endswith(".dot"):
      os.unlink(os.path.join(dir_arq, item))