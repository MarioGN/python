# declaração
meu_set = {1, 2, 3, 4, 5}
print(meu_set)

meu_set2 = set([1, 2, 3, 4, 5, 1])
print(meu_set2)

# criando um set vazio
meu_set = set([])

# add
meu_set.add(22)

# update
meu_set.update([1, 2, 3, 23, 24])
print(meu_set)

# discard
meu_set.discard(1)
print('discard: 1 -> ', meu_set)

# União
print('União')
print(meu_set | meu_set2)
print(meu_set.union(meu_set2))

# Intersecção
print('Intersecção')
print(meu_set & meu_set2)
print(meu_set.intersection(meu_set2))

# Diferença
print('Diferença')
print(meu_set - meu_set2)
print(meu_set.difference(meu_set2))

# Diferença simétrica
print('Diferença Simétrica')
print(meu_set ^ meu_set2)
print(meu_set.symmetric_difference(meu_set2))

# Criando um set utilizando comprehension
print('\n\nSet comprehension')
set_1 = {1, 2}
set_2 = {3, 4}

set_comp = {i for i in set_1.union(set_2)}
print(set_comp)

set_comp2 = {i * i for i in range(0, 10)}
print(set_comp2)


frozen_s = frozenset([1, 2, 3, 4])
print(frozen_s)
print(type(frozen_s)) 