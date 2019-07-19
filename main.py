#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from Parser import parser   

def main():
    param = sys.argv[1:]

    commit = param[0]
    dir_projeto = param[1]
    dir_result = param[2]
    localpath = param[3]
    nome_projeto = param[4]
  
    parser(commit, dir_projeto, dir_result, localpath, nome_projeto)

#-----------------------------------------------------
if __name__ == '__main__':
    main()
