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
    
       # print ('commit:', nomedocommit)
        #print('dir_projeto: ', dir_projeto)
        #print('dir_result: ', dir_result)
        #print ('localpath: ', localpath)
        #print('nome do projeto: ', nome_projeto)

    
        caminhoRaiz = leprojet(dir_projeto)
        #print('caminho raiz: 29', caminhoRaiz)
    
    #for i in caminhoRaiz:
     #   print('entreii')
    #    salvarcsv = listardiretorio(dir_result, ) # salvar csv: qual o diretorio
    
        
        Doxyfile_alterar_linha(dir_result + nome_projeto, dir_projeto + nome_projeto, localpath)
      
        
        #print('39')
        r = doxygen_Ex(localpath)
        #print('41')
       # print("salvar: ",salvarcsv,"i: ", i)
#        print('r: ',r)

        #for projeto in os.listdir(listardiretorio(dir_projeto,0)):
         #   pathprojeto = listardiretorio(dir_result,0)
         #   print('43 - todo os comites: ' + pathprojeto)
            #str(pathprojeto.replace('\\','/'))
          #  pathprojeto = pathprojeto.split('/')[-1]
        #    print('35 - todo os comites: ' + pathprojeto)
         
        while r == 0:

            delete(dir_result + nome_projeto + '/latex')
            print('nomedocommit: ', nomedocommit)
            
            with open( dir_result + nome_projeto + '/'+ nomedocommit +".csv", 'w', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';')
                    spamwriter.writerow(['PROJETO','COMMIT','ARQUIVO','CHAMADOR', ' CHAMADO']) # escreve st
                    
            for nomearquivo in os.listdir(dir_result + nome_projeto +'/latex'):
                if nomearquivo[-3:] != 'dot':
                    print('nome do arquivo',nomearquivo)
                    continue
                #  print('nome do arquivo: ', nomearquivo)       
                relation = {
                    'Node': {

                    },
                    'correlacao': [
                        
                    ]
                }
                arq = open(dir_result + nome_projeto + '/latex/'+ nomearquivo, 'r')
                texto2 = arq.readlines()
                #   print('nome do arquivo2: ', nomearquivo)  
            #  print('+++++++++++++++++++++++++++++++ separa chamador +++++++++++++++++++++++++++++++++++++++++++++++')
                #separa chamador
                for linha in texto2 :
                    chamado = re.search(r'(Node\d+) \[label=\"(.*?)\"', linha)
                    if chamado:
                        relation['Node'].update(dict({chamado.group(1): {}}))
                        relation['Node'][chamado.group(1)].update({'chamado': []})
                        relation['Node'][chamado.group(1)].update({'label' : chamado.group(2)})
           #     print('nome do arquivo 3: ', nomearquivo , 'nomedocommit: ', nomedocommit) 
                            
            # print('+++++++++++++++++++++++++++++++ separa chamados +++++++++++++++++++++++++++++++++++++++++++++++')
            #    print('nome do arquivo 4: ', nomearquivo, 'nomedocommit: ', nomedocommit)  
                #separa chamados
                for linha in texto2 :
                #    print("linha chamados: "+ linha) 
                    relacao = re.search(r'(Node\d+).*-> (Node\d+)', linha)
                    if relacao:
                        if relacao.group(1) in relation['Node']:
                            relation['Node'][relacao.group(1)]['chamado'].append(relacao.group(2))                        
                arq.close()
                
            #    print('nome do arquivo5: ', nomearquivo)    
            #print('====================== concatenas as relações chamador com chamados ======================================================')
                
                #concatenas as relações chamador com chamados
                for nodes in relation['Node']:
                    chamado = []
                    for x in relation['Node'][nodes]['chamado']:
                        chamado.append(relation['Node'][x]['label'])
                    relation['correlacao'].append(tuple((relation['Node'][nodes]['label'], chamado)))

                z = 0 
                for x in relation ['correlacao']:
                    if z < 1:
                        print(x[0],x[1])
                        z += 1
                                    
                print ("\n ")
                
         #       print('nome do arquivo 6: ', nomearquivo, 'nomedocommit: ', nomedocommit)
                  
          #      print('=================== salvando no arvivo csv : '+ nomedocommit +'  =====================================')
            # print('nome do arquivo7: ', nomearquivo)  
            # salvando no arvivo csv   
               # nomeprojeto = pathprojeto.split("\\")[-1]
                with open(dir_result + nome_projeto + '/'+ nomedocommit +".csv", 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';')
                    for x in relation ['correlacao']:
                        for k in x[1]:
                            spamwriter.writerow([nome_projeto, nomedocommit,nomearquivo,x[0],k]) 
                        break               
                arq.close()
            break
           
            #print('nome do arquivo9: ', nomearquivo)          
        deletatodos(dir_result + nome_projeto + '/latex')
        deletapasta(dir_result + nome_projeto)
            
    
            #arruma a identaçao while.
#parser('1 - de4c7d88f6a248e93d223173688368739e844ebe')
#parser('2 - 74d34e2b9c09d78dac45915833e4acc23926f58d')

