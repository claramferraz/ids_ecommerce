# Busca sequencial na lista encadeada

import time
from linkedlist import LinkedList
from data import IDsSearch

inicio = time.perf_counter()

def buscaSequencial(lista: LinkedList, chave):
    current = lista.firstNode
    indice = 0
    while current:
        if current.data == chave:
            return indice
        current = current.nextNode
        indice += 1
    return -1


def buscarIdsSequenciais(lista: LinkedList, ids_busca = None):
    if ids_busca is None:
        ids_busca = IDsSearch.ids_search

    resultados = []

    for id_busca in ids_busca:
        pos = buscaSequencial(lista, id_busca)
        resultados.append((id_busca, pos))
        if pos != -1:
            print(1)
        else:
            print(-1)

    return resultados

fim = time.perf_counter()

def salvarResultadosSequenciais(resultados):
    caminho = 'projeto_1_resultado_busca_sequencial.txt'
    try:
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            for _, pos in resultados:
                status = '1' if pos != -1 else '-1'
                arquivo.write(f"{status}\n")
        print(f"\nResultados salvos em: {caminho}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


if __name__ == '__main__':
    print("=== Busca Sequencial na Lista Encadeada ===\n")
    lista = LinkedList()
    lista.insertAllIds()
    resultados = buscarIdsSequenciais(lista)
    salvarResultadosSequenciais(resultados)
    print(f"Tempo: {fim - inicio:.8f} segundos")