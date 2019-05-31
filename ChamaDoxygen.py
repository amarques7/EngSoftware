#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

def doxygen_Ex(localpath):

  r = subprocess.call(["Doxygen.exe", localpath + "Doxyfile"])
  print( "R: ", r)
  return r