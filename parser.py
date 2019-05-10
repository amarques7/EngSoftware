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


#salvarcsv = listardiretorio('C:\Analysis',0)
caminhoRaiz = leprojet('C:\Analysis')

#print("salvar csv ",salvarcsv)
print("21 - caminho Raiz: ",caminhoRaiz)

for i in caminhoRaiz:
    salvarcsv = listardiretorio('C:\Analysis',0)
    print("25 - salvar csv ",salvarcsv)
  
   # Doxyfile_alterar_linha(salvarcsv,i)
    
   
    #apagar cogido da chamada do doxygen da linha 25 a 32
    #path = ('Excut_Dox.cmd')
    #print (path)
    #print(os.startfile(path))

    #print(os.getpid())
    #r = subprocess.call(["Excut_Dox.cmd", "-h"])
    #print(r)
####fim
    r = doxygen_Ex()
# delete (salvarcsv + '/latex')
    while houver passa:
        while r == 0:
        
            #delete("/Users/amarq/OneDrive/Desktop/documentacao/latex")
            delete(salvarcsv + '/latex')

            name_do_commit = listardiretorio('c:\Analysis', 1)
            name_do_commit = name_do_commit.split("\\")[-1]
            
            print('51 - dir : ', name_do_commit)
            
            with open(salvarcsv +'/'+ name_do_commit +".csv", 'w', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',')
                    spamwriter.writerow(['DIR','CHAMADOR', ' CHAMADO']) # escreve st
            
        
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
            
                with open(salvarcsv + '/'+ name_do_commit +'.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',')
                    for x in relation ['correlacao']:
                        for k in x[1]:
                            spamwriter.writerow([name_do_commit,x[0],k])
                            
                        break
                print('arquivo salvo: '+ salvarcsv+ '/'+name_do_commit+'.csv')
                arq.close()
            break
        deletapasta(listardiretorio('C:\Analysis',0))