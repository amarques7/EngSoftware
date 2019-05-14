#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re 
import csv
import os
import glob
import time
import subprocess

from ConfiguraDoxyfile  import Doxyfile_alterar_linha
from PercorreDiretorioEmProjetos import leprojet
from DeletaArquivo import delete
from ChamaDoxygen import doxygen_Ex
from ListarDiretorio import listardiretorio
from DeletaPasta import deletapasta 


def parser(nomedocommit):
        
        #salvarcsv = listardiretorio('C:\Analysis',0)
        caminhoRaiz = leprojet('C:\Repositorio')

        #print("salvar csv ",salvarcsv)
        print("21 - caminho Raiz: ",caminhoRaiz)


        for i in caminhoRaiz:
            salvarcsv = listardiretorio('C:\Resultado_1',0) # salvar csv: qual o diretorio
            print("25 - salvar csv ",salvarcsv)
            print ("I carregar o doxygen: ", i) 
        
            Doxyfile_alterar_linha(salvarcsv,i)
        # Doxyfile_alterar_linha(nova_linha_OUTPUT, nova_linha_INPUT)
            
        
            #apagar cogido da chamada do doxygen da linha 25 cls
            # a 32
            #path = ('Excut_Dox.cmd')
            #print (path)
            #print(os.startfile(path))

            #print(os.getpid())
            #r = subprocess.call(["Excut_Dox.cmd", "-h"])
            #print(r)
        ####fim
            r = doxygen_Ex()
        # delete (salvarcsv + '/latex')
        #  r= 0
            
            for projeto in os.listdir(listardiretorio('C:\Repositorio',0)):
                pathprojeto = listardiretorio('C:\Resultado_1',0)
                print('47 - todo os comites: ' + pathprojeto)
                str(pathprojeto.replace('\\','/'))
                pathprojeto = pathprojeto.split('/')[-1]
                print('51 - todo os comites: ' + pathprojeto)
                
                print ('56 - salvarcsv'+ salvarcsv)
                
                
                    
                while r == 0:
                
                    #delete("/Users/amarq/OneDrive/Desktop/documentacao/latex")
                    #delete(salvarcsv + '/latex')

                    name_do_commit = listardiretorio('c:\Repositorio', 1)
                    name_do_commit = name_do_commit.split("\\")[-1]
                #
                    
                    with open(salvarcsv +'/'+ nomedocommit +".csv", 'w', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=';')
                            spamwriter.writerow(['PROJETO','COMMIT','CHAMADOR', ' CHAMADO']) # escreve st
                            
                    for j in os.listdir(salvarcsv +'/latex'):
                        if j[-3:] != 'dot':
                            continue
                        relation = {
                            'Node': {

                            },
                            'correlacao': [
                                
                            ]
                        }
                        arq = open(salvarcsv + '/latex/'+j, 'r')
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
                        #    print("linha chamados: "+ linha) 
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

                        z = 0 
                        for x in relation ['correlacao']:
                            if z < 1:
                                print(x[0],x[1])
                                z += 1
                        
                    
                        print ("\n ")
                    
                        print('=================== salvando no arvivo csv  =====================================')
                    # salvando no arvivo csv   
                        print('129- nome do comitti:', nomedocommit )
                        nomeprojeto = pathprojeto.split("\\")[-1]
                        print ('130- nome do projeto: ', nomeprojeto )
                        with open(salvarcsv + '/'+ nomedocommit +'.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=';')
                            for x in relation ['correlacao']:
                                for k in x[1]:
                                    spamwriter.writerow([nomeprojeto, nomedocommit,x[0],k])
                                    
                                break
                        #print('arquivo salvo: '+ salvarcsv )
                        #print('arquivo salvo: '+ pathprojeto+'\\'+ nomedocommit +'.csv')
                        arq.close()
                    break 
                deletapasta(listardiretorio('C:\Repositorio',0))
            
        
            #arruma a identaçao while.
parser('1 - de4c7d88f6a248e93d223173688368739e844ebe')
parser('2 - 74d34e2b9c09d78dac45915833e4acc23926f58d')
parser('3 - 6c36ba6a769df6f0682501dba8aeb3d0b289cde2')
