from abc import ABC, abstractmethod


# Produto base
class Item(ABC):
    @abstractmethod
    def detalhes(self):
        pass


class Bebida(Item):
    def detalhes(self):
        return "Bebida refrescante"


class PratoPrincipal(Item):
    def detalhes(self):
        return "Prato principal delicioso"


# Factory Method
class ItemFactory:
    @staticmethod
    def criar_item(tipo: str) -> Item:
        if tipo == "bebida":
            return Bebida()
        elif tipo == "prato_principal":
            return PratoPrincipal()
        else:
            raise ValueError("Tipo de item desconhecido")
