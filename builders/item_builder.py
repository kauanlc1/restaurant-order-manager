# Classe do produto final
class PedidoPersonalizado:
    def __init__(self):
        self.itens = []
        self.acompanhamentos = []

    def __str__(self):
        return f"Pedido: {self.itens}, Acompanhamentos: {self.acompanhamentos}"

# Builder
class PedidoBuilder:
    def __init__(self):
        self.pedido = PedidoPersonalizado()

    def adicionar_item(self, item):
        self.pedido.itens.append(item)
        return self

    def adicionar_acompanhamento(self, acompanhamento):
        self.pedido.acompanhamentos.append(acompanhamento)
        return self

    def construir(self):
        return self.pedido
