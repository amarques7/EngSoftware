#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re 
import os
import sys

def main():
    param = sys.argv[1:]
    nova_linha_OUTPUT = param[0]
    localpath = param[1]
    nome_projeto = param[2]
   
    print("output: ", nova_linha_OUTPUT)
    print( "nome prj: ", nome_projeto)
    print("local: ", localpath)
    
    
    path = localpath + 'Doxyfile'
    with open("C:\Analise\modificado.txt",'r') as f:
        texto = f.readlines()
        nova_linha_INPUT =  ''.join(texto)


    nova_linha_INPUT ='INPUT                  = '+ nova_linha_INPUT
    nova_linha_OUTPUT = 'OUTPUT_DIRECTORY       = '+ nova_linha_OUTPUT + nome_projeto
    print("input: ", nova_linha_INPUT)
    print("output: ", nova_linha_OUTPUT)

    pasta = "C:\Analise"
    dir = os.listdir(pasta)

    for file in dir:
         if file == "modificado.txt":
             os.remove('{}/{}'.format(pasta, file))
    
    with open(path,'r') as f:
        texto = f.readlines()
    #print("entreio")
    while('#' not in texto[816]):
        #print("entreiww")
        del texto[816]

    with open(path,'w') as f:
        for i in texto:
        
            if texto.index(i) == 60:
                f.write(nova_linha_OUTPUT +'\n')
                
            elif texto.index(i) == 815:
                f.write(nova_linha_INPUT +'\n')
                
            else:
                f.write(i)
    
    return 0            
#-----------------------------------------------------
if __name__ == '__main__':
    main()
