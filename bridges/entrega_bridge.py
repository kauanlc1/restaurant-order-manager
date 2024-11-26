from abc import ABC, abstractmethod


# Implementação
class MetodoEntrega(ABC):
    @abstractmethod
    def entregar(self):
        pass


class Retirada(MetodoEntrega):
    def entregar(self):
        print("Pedido pronto para retirada.")


class Delivery(MetodoEntrega):
    def entregar(self):
        print("Pedido entregue no endereço.")


# Abstração
class Pedido:
    def __init__(self, metodo_entrega: MetodoEntrega):
        self.metodo_entrega = metodo_entrega

    def processar_entrega(self):
        self.metodo_entrega.entregar()
