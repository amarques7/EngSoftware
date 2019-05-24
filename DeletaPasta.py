import os
import shutil 
def deletapasta(dir):
  
    dir = dir +'/latex'
    
    os.removedirs(dir)

#deletapasta('C:/Resultado_1/BCC-2s13-PI2-Codigo-de-Honra')