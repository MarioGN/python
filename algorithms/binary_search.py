# BUSCA BINÁRIA
def bin_search(numbers, n):
    tamanho = len(numbers)

    resultado = -1
    inicio = 0
    fim = tamanho-1

    while inicio <= fim:
        meio = int((inicio+fim)/2)
        if numbers[meio] < n:
            inicio = meio+1
        elif numbers[meio] > n:
            fim = meio-1
        else:
            resultado = meio
            break

    return resultado


numeros = [1, 2, 3, 4, 7, 8, 9]
print(numeros)
print(bin_search(numeros, 4))
print(bin_search(numeros, 1))
print(bin_search(numeros, 9))
print(bin_search(numeros, 2))