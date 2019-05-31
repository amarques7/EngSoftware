#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def leprojet(projetos):
    todoscommit=[]
    
    for projeto in os.listdir(projetos):
        pathprojeto = projetos +  projeto
        todoscommit.append( pathprojeto)
    
    return todoscommit