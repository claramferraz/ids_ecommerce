#Busca binária para encontrar um ID pelo seu vetor

import time
from data import IDsSearch, IDsProjeto
from vector import vetorized_ids

inicio = time.perf_counter()

def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        
        if lista[pos_meio] == chave:
            return pos_meio
        
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        
        if lista[pos_meio] < chave:
            pos_ini = pos_meio + 1
    
    return -1


def buscarIdsVetorizados(ids_busca = None):
    if ids_busca is None:
        ids_busca = IDsSearch.ids_search
    
    # Cria lista de pares (vetor, id_original) e ordena pelos vetores
    pares_vetor_id = []
    for i, vetor in enumerate(vetorized_ids):
        if i < len(IDsProjeto.ids_projeto):
            pares_vetor_id.append((vetor, IDsProjeto.ids_projeto[i]))
    
    pares_vetor_id.sort(key=lambda x: x[0])
    lista_ordenada = [par[0] for par in pares_vetor_id]
    
    resultados = []
    
    for id_busca in ids_busca:
        # Vetoriza o ID de busca
        try:
            chave = [int(char) for char in id_busca]
        except ValueError:
            chave = []
        
        # Realiza busca binária
        posicao = buscaBinaria(lista_ordenada, chave)
        resultados.append((id_busca, posicao))
        
        # Imprime resultado
        if posicao != -1:
            id_encontrado = pares_vetor_id[posicao][1]
            print(1)
        else:
            print(-1)
    
    return resultados
fim = time.perf_counter()

def salvarResultados(resultados):
    projeto_1_resultado_busca_binaria = 'projeto_1_resultado_busca_binaria.txt'
    
    try:
        with open(projeto_1_resultado_busca_binaria, 'w', encoding='utf-8') as arquivo:
            for id_busca, posicao in resultados:
                status = '1' if posicao != -1 else '-1'
                arquivo.write(f"{status}\n")
        print(f"\nResultados salvos em: {projeto_1_resultado_busca_binaria}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


if __name__ == '__main__':
    print("=== Busca Binária Vetorizada ===\n")
    resultados = buscarIdsVetorizados()
    salvarResultados(resultados)
    print(f"Tempo: {fim - inicio:.8f} segundos")


