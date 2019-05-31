#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re 
import os
import sys 


def main():
    param = sys.argv[1:]

    nova_linha_INPUT = param[0]
    nova_linha_OUTPUT = param[1]
    localpath = param[2]
    nome_projeto = param[3]

    print ("entrei")

    path = localpath + 'Doxyfile'
    print(path)
    nova_linha_OUTPUT = 'OUTPUT_DIRECTORY       = '+ nova_linha_OUTPUT + nome_projeto
    nova_linha_INPUT ='INPUT                  = '+ nova_linha_INPUT + nome_projeto
    
    with open(path,'r') as f:
        texto=f.readlines()

    with open(path,'w') as f:
        for i in texto:
            if texto.index(i)==60:
                f.write(nova_linha_OUTPUT+'\n')

            elif texto.index(i)==815:
                f.write(nova_linha_INPUT+'\n')

            else:
                f.write(i)
   
    return 0            
#-----------------------------------------------------
if __name__ == '__main__':
    main()
