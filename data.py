#Importar lista de IDs de um arquivo de texto

class IDsProjeto:
    projeto1_ids = 'projeto_1_lista_IDs_entrada.txt'

    ids_projeto = []

    try:
        with open(projeto1_ids, 'r') as arquivo:
            for linha in arquivo:
                dado_limpo = linha.strip()
                
                ids_projeto.append(dado_limpo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{projeto1_ids}' não foi encontrado.")

class IDsSearch:
    projeto1_ids_search = 'projeto_1_lista_IDs_busca.txt'

    ids_search = []

    try:
        with open(projeto1_ids_search, 'r') as arquivo:
            for linha in arquivo:
                dado_limpo = linha.strip()
                
                ids_search.append(dado_limpo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{projeto1_ids_search}' não foi encontrado.")