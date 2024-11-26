from abc import ABC, abstractmethod


# Componente base
class ItemMenu(ABC):
    @abstractmethod
    def exibir(self):
        pass


# Item individual
class Item(ItemMenu):
    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        print(self.nome)


# Grupo de itens
class Categoria(ItemMenu):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item: ItemMenu):
        self.itens.append(item)

    def exibir(self):
        print(f"Categoria: {self.nome}")
        for item in self.itens:
            item.exibir()
