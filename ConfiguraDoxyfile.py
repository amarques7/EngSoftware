
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re 
import os

def Doxyfile_alterar_linha(nova_linha_OUTPUT, nova_linha_INPUT ):

    path = 'Doxyfile'
    nova_linha_OUTPUT = 'OUTPUT_DIRECTORY       = '+ nova_linha_OUTPUT
    nova_linha_INPUT ='INPUT                  = '+ nova_linha_INPUT

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
                
#alterar_linha( path = 'Doxyfile.txt',index_linha = '815',nova_linha ='INPUT                  = C:/Users/amarq/OneDrive/Desktop/linux-master')