from abc import ABC, abstractmethod


class EstadoPedido(ABC):
    @abstractmethod
    def proximo(self, pedido):
        pass


class Novo(EstadoPedido):
    def proximo(self, pedido):
        print("Pedido está em preparação.")
        pedido.estado = EmPreparacao()


class EmPreparacao(EstadoPedido):
    def proximo(self, pedido):
        print("Pedido está pronto.")
        pedido.estado = Pronto()


class Pronto(EstadoPedido):
    def proximo(self, pedido):
        print("Pedido já está pronto para entrega.")


class Pedido:
    def __init__(self):
        self.estado = Novo()

    def avancar(self):
        self.estado.proximo(self)
