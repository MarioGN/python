from vetores import vetor
from listas_ligadas import lista_ligada


if __name__ == "__main__":
    lklist = lista_ligada.ListaLigada()
    print(lklist.vazia())

    lklist.inserir(1)
    lklist.inserir(3)
    lklist.inserir(2)
    lklist.inserir(5)
    lklist.inserir(16)

    print(lklist)

    # print(lklist.recuperar_no(-1))
    # print(lklist.recuperar_no(6))
    # print(lklist.recuperar_no(3).elemento)

    print(lklist.recuperar_elemento(-1))
    print(lklist.recuperar_elemento(6))
    print(lklist.recuperar_elemento(3))

    lklist.inserir_na_posicao(-1, 99)
    lklist.inserir_na_posicao(100, 20)
    lklist.inserir_na_posicao(2, 29)
    lklist.inserir_na_posicao(4, 4)
    print('\n\n', lklist)

    print(lklist.contem(3))
    print(lklist.contem(16))
    print(lklist.contem(233))

    print(lklist.indice(3))
    print(lklist.indice(16))
    print(lklist.indice(233))

    print(lklist)
    lklist.remover_posicao(-1)
    lklist.remover_posicao(30)
    lklist.remover_posicao(0)
    lklist.remover_posicao(5)
    lklist.remover_posicao(2)

    lklist.remover_elemento(300)
    lklist.remover_elemento(4)
    print(lklist)


    # v = vetor.Vetor()

    # v.inserir_elemento_idx(10, 0)
    # v.inserir_elemento_idx(8, 1)
    # v.inserir_elemento_idx(30, 2)
    # v.inserir_elemento_idx(12, 3)
    # v.inserir_elemento_idx(3, 5)

    # print(v)
    # print('tamanho: ', v.tamanho())
    # print('elemento 3 ->', v.listar_elemento(3))
    
    # print('contem 20', v.contem(20))
    # print('contem 30 ->', v.contem(30))

    # print('idx 20 -> ', v.indice(20))
    # print('idx 30 -> ', v.indice(30))

    # v.remover_elemento_idx(2)
    # print(v)
    # v.remover_elemento_idx(10)
    # print(v)

    # # v.remover_elemento(10)
    # # print(v)
    # # v.remover_elemento(99)
    # # print(v)
