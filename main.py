#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from Parser import parser   
from ConfiguraDoxyfile  import Doxyfile_alterar_linha

def main():
    param = sys.argv[1:]

    commit = param[0]
    dir_projeto = param[1]
    dir_result = param[2]
    localpath = param[3]
    nome_projeto = param[4]

   # Doxyfile_alterar_linha(dir_result + nome_projeto, dir_projeto + nome_projeto, "C:\Users\amarq\eclipse-workspace\ParseLine")    
    parser(commit, dir_projeto, dir_result, localpath, nome_projeto)

#-----------------------------------------------------
if __name__ == '__main__':
    main()
