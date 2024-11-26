# Sistema existente
class SistemaPagamento:
    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor} processado no sistema legado.")


# Novo sistema de pagamento
class NovoSistemaPagamento:
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado no novo sistema.")


# Adapter
class PagamentoAdapter:
    def __init__(self, novo_sistema: NovoSistemaPagamento):
        self.novo_sistema = novo_sistema

    def processar_pagamento(self, valor):
        self.novo_sistema.pagar(valor)
