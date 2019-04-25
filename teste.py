
#name = input ('What'+"'s"+ 'your name? ')
#weight = input ('What'+"'s"+ 'your weight?')
#age = input ('What'+"'s"+ 'your age?')
#day = input('dia que nasceu? ')
#mes = input('mes que nasceu? ')
#ano = input('ano que nasceu? ')
#print(name + ' vc nasceu no dia '+ day,'de', mes,'de' ,ano)

#numero_a = input('Digite um número:\n ')
#numero_b = input('Digite outro número:\n ')
#soma = int(numero_a) + int(numero_b,)
#print(type(numero_a), type(numero_b), type(soma))
#print('A soma de {}  e {} vale {}'.format(numero_a, numero_b, soma)

#n = int(input('digite algo: '))

#if n.isnumeric():
#print(type(n))
   # print(type(n % 2))
#if (n % 2) == 0:
 #   print('par')
#else:
 #   print('O número {:=^30}'.format(n), 'é impar')
#else:
 #   print('nao é número: ')



testedict = {
    'Node': {
        'Node54':{
            'chamado': ['Node55', 'Node56'],
            'label': 'cpio_trailer'
        },
        'Node55':{
            'chamado': ['Node56'],
            'label': 'push_hdr'
        },
        'Node56':{
            'chamado': [],
            'label': 'push_xxx'
        }
    },
    'cor': [
        
    ]
}

#uma = testedict['Node']['Node54']['chamado'] 
print('==================================================')

for nodes in testedict['Node']:
    chamado = []
    for x in testedict['Node'][nodes]['chamado']:
        chamado.append(testedict['Node'][x]['label'])
    testedict['cor'].append(tuple((testedict['Node'][nodes]['label'], chamado)))

print (testedict['cor'])

#print (testedict['Node']['1'], testedict['numero']['2'], testedict['numero']['3'])
#print(testedict)