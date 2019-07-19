#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re 
import csv
import os
import glob
import time
import subprocess
import sys

from ConfiguraDoxyfile  import Doxyfile_alterar_linha
from PercorreDiretorioEmProjetos import leprojet
from DeletaArquivo import delete
from ChamaDoxygen import doxygen_Ex
from ListarDiretorio import listardiretorio
from DeletaTodos import deletatodos
from DeletaPasta import deletapasta 

def parser(nomedocommit, dir_projeto, dir_result, localpath, nome_projeto):

    caminhoRaiz = leprojet(dir_projeto)

    print("entrei")
    r=0
    while r == 0:
        print("entreiwile")
        delete(dir_result + nome_projeto + '/latex')
        
        with open( dir_result + nome_projeto + '/'+ nomedocommit +".csv", 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';')
                spamwriter.writerow(['PROJETO','COMMIT','ARQUIVO','CHAMADOR', ' CHAMADO']) # escreve st
                
        for nomearquivo in os.listdir(dir_result + nome_projeto +'/latex'):
            print("entrei for")
            if nomearquivo[-3:] != 'dot': 
                continue            
            relation = {
                'Node': {

                },
                'correlacao': [
                    
                ]
            }
         
            arq = open(dir_result + nome_projeto + '/latex/'+ nomearquivo, 'r')
            texto2 = arq.readlines()  

        #  print('+++++++++++++++++++++++++++++++ separa chamador +++++++++++++++++++++++++++++++++++++++++++++++')
            #separa chamador
            for linha in texto2 :
                chamado = re.search(r'(Node\d+) \[label=\"(.*?)\"', linha)
                if chamado:
                    relation['Node'].update(dict({chamado.group(1): {}}))
                    relation['Node'][chamado.group(1)].update({'chamado': []})
                    relation['Node'][chamado.group(1)].update({'label' : chamado.group(2)})
                                    
        # print('+++++++++++++++++++++++++++++++ separa chamados +++++++++++++++++++++++++++++++++++++++++++++++')
            #separa chamados
            for linha in texto2 :          
                relacao = re.search(r'(Node\d+).*-> (Node\d+)', linha)
                if relacao:
                    if relacao.group(1) in relation['Node']:
                        relation['Node'][relacao.group(1)]['chamado'].append(relacao.group(2))                        
            arq.close()       
        #print('====================== concatenas as relações chamador com chamados ======================================================')
            #concatenas as relações chamador com chamados
            for nodes in relation['Node']:
                chamado = []
                for x in relation['Node'][nodes]['chamado']:
                    chamado.append(relation['Node'][x]['label'])
                relation['correlacao'].append(tuple((relation['Node'][nodes]['label'], chamado)))

            #z = 0 
            #for x in relation ['correlacao']:
             #   if z < 1:
              #      print(x[0],x[1])
               #     z += 1
                                
            #print ("\n ")            
            #salvando no arvivo csv 
            nomearquivo = nomearquivo[:-46]
            with open(dir_result + nome_projeto + '/'+ nomedocommit +".csv", 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';')
                for x in relation ['correlacao']:
                    for k in x[1]:
                        spamwriter.writerow([nome_projeto, nomedocommit,nomearquivo,x[0],k]) 
                    break               
            arq.close()
        break
  #  deletatodos(dir_result + nome_projeto + '/latex')
   # deletapasta(dir_result + nome_projeto)