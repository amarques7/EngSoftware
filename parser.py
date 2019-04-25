#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re 
import csv
y = 1
while (y <= 16):
    print ('entrei no while')

    arq = open(str(y)+'gen.dot', 'r')
    texto2 = arq.readlines()

    testedict = {
        'Node': {

        },
        'cor': [
            
        ]
    }
    #separa chamador
    for linha in texto2 :
        chamado = re.search(r'(Node\d+).*label=\"(.*?)\"', linha)
        if chamado:
            testedict['Node'].update(dict({chamado.group(1): {}}))
            testedict['Node'][chamado.group(1)].update({'chamado': []})
            testedict['Node'][chamado.group(1)].update({'label' : chamado.group(2)})

    #separa chamados
    for linha in texto2 :
        relacao = re.search(r'(Node\d+).*-> (Node\d+)', linha)

        if relacao:
            if relacao.group(1) in testedict['Node']:
                testedict['Node'][relacao.group(1)]['chamado'].append(relacao.group(2))
    arq.close()
    print('==================================================')

    #concatenas as relações chamador com chamados
    for nodes in testedict['Node']:
        chamado = []
        for x in testedict['Node'][nodes]['chamado']:
            chamado.append(testedict['Node'][x]['label'])
        testedict['cor'].append(tuple((testedict['Node'][nodes]['label'], chamado)))

    for x in testedict ['cor']:
        print(x)
    #print (testedict['cor'])

    print ("\n ")
    #salva em .csv
    with open(str(y)+'gen.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['CHAMADOR', ' CHAMADO']) # escreve st

    with open(str(y)+'gen.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for x in testedict ['cor']:
            spamwriter.writerow([x[0]]) # escreve strings no csv
            for k in x[1]:
                spamwriter.writerow([',',k])
    y += 1
