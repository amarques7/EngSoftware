#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re 
import csv
arq = open('gen.dot', 'r')
#texto = arq.read()
texto2 = arq.readlines()


testedict = {
    'Node': {

    },
    'cor': [
        
    ]
}

for linha in texto2 :
    #print(linha)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")    
    chamado = re.search(r'(Node\d+).*label=\"(.*?)\"', linha)
    
    if chamado:
        print('--------no node CHAMADO-----')
        print(chamado.group(1)) 
        
        testedict['Node'].update(dict({chamado.group(1): {}}))

        testedict['Node'][chamado.group(1)].update({'chamado': []})
        testedict['Node'][chamado.group(1)].update({'label' : chamado.group(2)})
        
        print(chamado.group(2))

print ('\n\n---- breakpoint\n')
print (testedict)
print ('\n---- breakpoint\n\n')

for linha in texto2 :
    relacao = re.search(r'(Node\d+).*-> (Node\d+)', linha)

    if relacao:
        if relacao.group(1) in testedict['Node']:
            testedict['Node'][relacao.group(1)]['chamado'].append(relacao.group(2))


print ('\n\n---- breakpoint\n')
print (testedict)
print ('\n---- breakpoint\n\n')

    
#print(texto)
arq.close()
#######
#chamado = re.compile(r'Node\d++).*label="(.*?)"')

#chamado = re.search(r'(Node\d+).*label=\"(.*?)\"', texto)
#relacao = re.search(r'(Node\d+).*-> (Node\d+)', texto)
#print('############## chamador ###########################')
#print(chamado.group(1))
#print(chamado.group(2))
#print('############## chamado ##########################')
#print(relacao.group(1))
#print(relacao.group(2))
#(Node\d++).*-> (Node\d++)

print('==================================================')

for nodes in testedict['Node']:
    chamado = []
    for x in testedict['Node'][nodes]['chamado']:
        chamado.append(testedict['Node'][x]['label'])
    testedict['cor'].append(tuple((testedict['Node'][nodes]['label'], chamado)))

print (testedict['cor'])

# abrindo o arquivo para escrita
with open('teste.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam']) # escreve tres strings no cs

