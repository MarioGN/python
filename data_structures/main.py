from vetores import vetor


if __name__ == "__main__":
    v = vetor.Vetor()

    v.inserir_elemento_idx(10, 0)
    v.inserir_elemento_idx(8, 1)
    v.inserir_elemento_idx(30, 2)
    v.inserir_elemento_idx(12, 3)
    v.inserir_elemento_idx(3, 5)

    print(v)
    print('tamanho: ', v.tamanho())
    print('elemento 3 ->', v.listar_elemento(3))
    
    print('contem 20', v.contem(20))
    print('contem 30 ->', v.contem(30))

    print('idx 20 -> ', v.indice(20))
    print('idx 30 -> ', v.indice(30))

    v.remover_elemento_idx(2)
    print(v)
    v.remover_elemento_idx(10)
    print(v)

    # v.remover_elemento(10)
    # print(v)
    # v.remover_elemento(99)
    # print(v)
