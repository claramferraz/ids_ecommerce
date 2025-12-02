#Classe para criar a lista encadeada

from node import Node
from data import IDsProjeto

class LinkedList:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None

    def insertAtBegin(self, value):
        newNode = Node(value)
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            newNode.nextNode = self.firstNode
            self.firstNode = newNode

    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            self.lastNode.nextNode = newNode
            self.lastNode = newNode

    def insertAllIds(self):
        #Adiciona todos os IDs do arquivo à lista encadeada
        for id in IDsProjeto.ids_projeto:
            self.insertAtEnd(id)

    def viewList(self):
        #Exibe todos os nós da lista encadeada
        if self.firstNode is None:
            print("Lista vazia")
            return
        
        current = self.firstNode
        count = 0
        while current:
            print(f"[Nó {count}] data: {current.data} | próximo: ", end="")
            if current.nextNode:
                print(f"[Nó {count + 1}]")
            else:
                print("None")
            current = current.nextNode
            count += 1

