from vetores import vetor
from listas_ligadas import lista_ligada, lista_duplamente_ligada
from pilhas import pilha
from filas import fila
from conjuntos import conjunto
from espalhamento import tabela_espalhamento
from mapas import mapa


if __name__ == "__main__":
    mp = mapa.Mapa(5)
    print(mp)

    mp.adicionar("cliente01", 'josé')
    mp.adicionar("cliente03", 'maria')
    mp.adicionar("cliente04", 'augusto')
    mp.adicionar("cliente05", 'carla')
    mp.adicionar("cliente06", 'joão')
    mp.adicionar("cliente07", 'aparecida')
    print(mp)

    print('cliente removido: ', mp.remover('cliente01'))
    print(mp)

    mp.adicionar('cliente01', 'joão')
    print('\n\n',mp)

    mp.adicionar('cliente01', 'joão atualizado')
    print('\n\n',mp)

    print(mp.recuperar('cliente01'))
    print(mp.recuperar('chaveinvalida'))
    
    # tbl = tabela_espalhamento.TabelaEspalhamento()

    # tbl.inserir(1)
    # tbl.inserir(12)
    # tbl.inserir(277)
    # tbl.inserir(999)
    # tbl.inserir(658)
    # tbl.inserir(85)
    # tbl.inserir(9)
    # print(tbl)

    # tbl.remover(1)
    # tbl.remover(87)
    # tbl.remover(999)
    # tbl.remover(277)
    # tbl.remover(12)
    # print(tbl)
    
    
    # conj = conjunto.Conjunto()
    # print('Set vazio: ', conj.vazia())

    # conj.inserir(1)
    # conj.inserir(2)
    # conj.inserir(3)
    # conj.inserir(4)
    # conj.inserir(5)

    # conj.inserir(4)
    # conj.inserir(4)
    
    # conj.inserir_posicao(0, 43)
    # conj.inserir_posicao(3, 22)
    # conj.inserir_posicao(7, 9)


    # print('Conjunto -> ', conj)
    
    # f = fila.Fila()
    # print('Fila vazia: ', f.vazia())

    # f.inserir(1)
    # f.inserir(2)
    # f.inserir(3)

    # print(f)

    # print('Fila vazia: ', f.vazia())

    # print(f.remover())
    # print(f.remover())
    # print(f.remover())
    # print(f.remover())

    # f.inserir(4)
    # f.inserir(5)
    # print(f.remover())
    # print(f)


    # pl = pilha.Pilha()
    
    # print('Pilha vazia: ', pl.vazia())

    # pl.empilhar(1)
    # pl.empilhar(2)
    # pl.empilhar(3)
    # pl.empilhar(4)
    # pl.empilhar(5)
    # print('Pilha: ', pl)

    # print(pl.desempilhar())
    # print(pl.desempilhar())
    # print(pl.desempilhar())
    # print(pl.desempilhar())
    # print(pl.desempilhar())
    # print(pl.desempilhar())
    # print(pl.desempilhar())
    
    # print('\n\n', pl)
    # print('Pilha vazia: ', pl.vazia())

    # ldup = lista_duplamente_ligada.ListaDuplamenteLigada()
    # print('Lista vazia:', ldup.vazia())

    # ldup.inserir(1)
    # ldup.inserir(2)
    # ldup.inserir(3)
    # ldup.inserir(4)
    # ldup.inserir(5)
    # print('Lista vazia:', ldup.vazia())
    # print(ldup)
    
    # ldup.inserir_na_posicao(0, 0)
    # ldup.inserir_na_posicao(6, 99)
    # ldup.inserir_na_posicao(3, 29)
    # print(ldup)

    # print('idx 0: ', ldup.recuperar_elemento(0))
    # print('idx 2: ', ldup.recuperar_elemento(2))
    # print('idx 7: ', ldup.recuperar_elemento(7))

    # print('contem "0"', ldup.contem(0))
    # print('contem "150"', ldup.contem(150))
    # print('contem "3"', ldup.contem(3))

    # print('idx de "0" ->', ldup.indice(0))
    # print('idx de "150" ->', ldup.indice(150))
    # print('idx de "3" ->', ldup.indice(3))

    # ldup.remover_posicao(-1)
    # ldup.remover_posicao(8)
    # ldup.remover_posicao(0)
    # ldup.remover_posicao(6)
    # ldup.remover_posicao(2)
    # print(ldup)

    # ldup.remover_elemento(3)
    # ldup.remover_elemento(5)
    # print(ldup)

    # lklist = lista_ligada.ListaLigada()
    # print(lklist.vazia())

    # lklist.inserir(1)
    # lklist.inserir(3)
    # lklist.inserir(2)
    # lklist.inserir(5)
    # lklist.inserir(16)

    # print(lklist)

    # lklist.inserir_na_posicao(-1, 20)
    # lklist.inserir_na_posicao(10, 220)
    # lklist.inserir_na_posicao(0, 0)
    # lklist.inserir_na_posicao(6, 89)
    # lklist.inserir_na_posicao(4, 44)
    # print(lklist)

    # # print(lklist.recuperar_no(-1))
    # # print(lklist.recuperar_no(6))
    # # print(lklist.recuperar_no(3).elemento)

    # print(lklist.recuperar_elemento(-1))
    # print(lklist.recuperar_elemento(6))
    # print(lklist.recuperar_elemento(3))

    # lklist.inserir_na_posicao(-1, 99)
    # lklist.inserir_na_posicao(100, 20)
    # lklist.inserir_na_posicao(2, 29)
    # lklist.inserir_na_posicao(4, 4)
    # print('\n\n', lklist)

    # print(lklist.contem(3))
    # print(lklist.contem(16))
    # print(lklist.contem(233))

    # print(lklist.indice(3))
    # print(lklist.indice(16))
    # print(lklist.indice(233))

    # print(lklist)
    # lklist.remover_posicao(-1)
    # lklist.remover_posicao(30)
    # lklist.remover_posicao(0)
    # lklist.remover_posicao(5)
    # lklist.remover_posicao(2)

    # lklist.remover_elemento(300)
    # lklist.remover_elemento(4)
    # print(lklist)


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
