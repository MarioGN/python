ls_inteiros = [1, 2, 3, 4, 5]
ls_string = ['Olá', 'Mundo!']
ls_mesclada = [1, 2, 3, 'Olá', 'Mundo!', 4, 5]
nested_list = [[1, 2, 3], [True, False, ['Python']]]

print(ls_inteiros)
print(ls_string)
print(ls_mesclada)
print(nested_list)

# len() -> tamanho da lista
tamanho = len(ls_mesclada)
print('tamanho da lista "ls_mesclada" -> ', tamanho)

# append(e) -> insere no final da lista
print('inteiros -> ', ls_inteiros)
ls_inteiros.append(6)
print('inteiros -> ', ls_inteiros)

# insert(posicao, e) -> insere elemento na posição
ls_string.insert(0, 'Python')
print(ls_string)

# remove(e) -> remove elemento da lista
ls_string.remove('Python')
print(ls_string)

# count(e) -> conta quantas vezes um elemento aparece na lista
c = ls_inteiros.count(2)
print('count "2" -> ', c)
ls_inteiros.append(2)
ls_inteiros.append(2)
c = ls_inteiros.count(2)
print('count "2" -> ', c)

# sort()
ls_inteiros.sort(reverse=True)
print(ls_inteiros)
ls_inteiros.sort()
print(ls_inteiros)

import copy
# Deep copy -> copia o conteúdo da lista
nova_lista = copy.deepcopy(nested_list)
nova_lista[0][1] = 'deepcopy'

print('\n\noriginal', nested_list)
print('copia (deepcopy)', nova_lista)

# Shallow copy -> copia a referência
nova_lista2 = copy.copy(nested_list)
nova_lista2[0][1] = 'shallowcopy'
print('\noriginal', nested_list)
print('copia (shallowcopy)', nova_lista2)


# List comprehension
mult = [1, 2, 3, 4, 8, 14]

nova = []
for i in mult:
    nova.append(i * i)
print(nova)

nova_comp = [i * i for i in mult]
print(nova_comp)

# Slice
nums = [1, 2, 3, 4, 8, 14, 28, 2]
print('\n\nlista: ', nums)
print('[0:4]', nums[0:4])
print('[1:]', nums[1:])
print('[:3]', nums[:3])
print('[0:4]', nums[0:4])

intervalo = slice(1, 4)
print(intervalo)

# Arrays
from array import array


array_int = array('B', [1, 2, 3, 4, 5])
print('\n\n', array_int)

for i in array_int:
    print(i)

# Remove(e)
array_int.remove(2)
print(array_int.tolist())

# Index(e)
print(array_int.index(1))

# Atualizar dados
array_int[1] = 2
print(array_int.tolist())