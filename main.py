from linkedlist import LinkedList
from search import sequentialSearch

# Criar lista encadeada
lista = LinkedList()

# Adicionar todos os IDs do arquivo
lista.insertAllIds()

# Exibir a lista encadeada
print("=== Lista Encadeada ===\n")

# Mostrar apenas os primeiros 20 elementos para não sobrecarregar
current = lista.firstNode

elementos = []
while current:
    elementos.append(str(current.data))
    current = current.nextNode
    
print(" → ".join(elementos) + " → None")

# Mostrar total de nós
total = 0
current = lista.firstNode
while current:
    total += 1
    current = current.nextNode

print(f"Total de nós na lista: {total}")
print(f"\nPrimeiro nó: {lista.firstNode.data}")
print(f"Último nó: {lista.lastNode.data}")

sequentialSearch(lista)


