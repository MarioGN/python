minha_tupla = (1, 2, 3, 'Python', 1.5)
minha_tupla2 = 1, 2, 3, 'Python', 1.5

print('tp 1:', minha_tupla)
print('tp 2:', minha_tupla2)

# count
print(minha_tupla.count(2))

# index
print('"Python" index -> ', minha_tupla.index('Python'))

# verificar existencia
print('Python na tupla ->', 'Python' in minha_tupla)

nova_ = minha_tupla.__add__(minha_tupla2)
print(nova_)
