# clientes = dict({1: 'Augusto', 2: 'José', 3: 'Aparecida'})
clientes = {1: 'Augusto', 2: 'José', 3: 'Aparecida'}

print(clientes)
print(type(clientes))

print('1 -> ', clientes[1])
print('2 -> ', clientes[2])

print('\n\nValores')
for cli in clientes.items():
    print(cli)

print('\n\n[chave, valor]')
for cod, nome in clientes.items():
    print(f'{cod} -> {nome}')

# operações
# get
print(clientes.get(3))

# len()
print('tamanho do dict: ', len(clientes))

# pop()
print('pop: ', clientes.pop(2))

# keys
print('keys-> ', clientes.keys())

# add
clientes[4] = 'João'
clientes.update({5: 'Maria'})
print(clientes)

# clear()
clientes.clear()
print('dict clear: ', clientes)