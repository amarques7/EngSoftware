#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re 
import csv

filepath = "C:\Codigos\Engenharia_Software"
dirname = filepath.split("\\")[-1]

with open(str(dirname)+".csv", 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['DIR','CHAMADOR', ' CHAMADO']) # escreve st
y = 1
while (True):
    if y is 17:
        break

    relation = {
        'Node': {

        },
        'correlacao': [
            
        ]
    }
    arq = open(str(y)+'gen.dot', 'r')
    texto2 = arq.readlines()

    #separa chamador
    for linha in texto2 :
        chamado = re.search(r'(Node\d+).*label=\"(.*?)\"', linha)
        if chamado:
            relation['Node'].update(dict({chamado.group(1): {}}))
            relation['Node'][chamado.group(1)].update({'chamado': []})
            relation['Node'][chamado.group(1)].update({'label' : chamado.group(2)})

    #separa chamados
    for linha in texto2 :
        relacao = re.search(r'(Node\d+).*-> (Node\d+)', linha)

        if relacao:
            if relacao.group(1) in relation['Node']:
                relation['Node'][relacao.group(1)]['chamado'].append(relacao.group(2))
    arq.close()
    print('==================================================')

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
# salvando no arvivo csv   
    with open(str(dirname)+".csv", 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for x in relation ['correlacao']:
            for k in x[1]:
                spamwriter.writerow([dirname,x[0],k])
            break
    y += 1
