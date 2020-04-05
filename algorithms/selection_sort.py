# SELECTION SORT
#   melhor caso: O(1)
#   pior caso: O(n)

def sel_sort(numeros):
    tamanho = len(numeros)
    for i in range(tamanho):
        idx_menor = i
        for j in range(i + 1, tamanho):
            if numeros[j] < numeros[idx_menor]:
                idx_menor = j

        aux = numeros[idx_menor]
        numeros[idx_menor] = numeros[i]
        numeros[i] = aux


numeros = [2, 7, 8, 4, 9, 1, 3]
print(numeros)
sel_sort(numeros)
print(numeros)
