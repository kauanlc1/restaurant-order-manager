class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def notificar(self, mensagem):
        print(f"Notificação para {self.nome}: {mensagem}")


class Pedido:
    def __init__(self):
        self.status = "Novo"
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def atualizar_status(self, novo_status):
        self.status = novo_status
        self.notificar_observadores()

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.notificar(f"Pedido agora está {self.status}")
