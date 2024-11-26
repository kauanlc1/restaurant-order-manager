class Handler:
    def __init__(self, proximo=None):
        self.proximo = proximo

    def handle(self, pedido):
        if self.proximo:
            self.proximo.handle(pedido)


class NovoHandler(Handler):
    def handle(self, pedido):
        if pedido.status == "novo":
            print("Processando pedido novo...")
        super().handle(pedido)


class PreparacaoHandler(Handler):
    def handle(self, pedido):
        if pedido.status == "em preparação":
            print("Preparando pedido...")
        super().handle(pedido)


class ProntoHandler(Handler):
    def handle(self, pedido):
        if pedido.status == "pronto":
            print("Pedido pronto para entrega.")
        super().handle(pedido)
