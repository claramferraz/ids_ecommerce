#Vetorização de IDs

from data import IDsProjeto

vetorized_ids = []

for id in IDsProjeto.ids_projeto:
    vetorized_id = [int(char) for char in id]
    print(f"ID Original: {id} -> ID Vetorizado: {vetorized_id}")

    vetorized_ids.append(vetorized_id)
