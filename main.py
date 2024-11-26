from factories.item_factory import ItemFactory
from factories.item_abstract_factory import ComidaItalianaFactory, ComidaFastFoodFactory
from builders.item_builder import PedidoBuilder
from adapters.pagamento_adapter import SistemaPagamento, NovoSistemaPagamento, PagamentoAdapter
from bridges.entrega_bridge import Pedido as PedidoEntrega, Retirada, Delivery
from models.menu import Item, Categoria
from chains.processador_pedidos import NovoHandler, PreparacaoHandler, ProntoHandler
from states.estados_pedido import Pedido as PedidoEstado


def main():
    # 1. Factory Method
    print("\n=== Factory Method ===")
    item_bebida = ItemFactory.criar_item("bebida")
    item_prato = ItemFactory.criar_item("prato_principal")
    print(item_bebida.detalhes())
    print(item_prato.detalhes())

    # 2. Abstract Factory
    print("\n=== Abstract Factory ===")
    fast_food_factory = ComidaFastFoodFactory()
    italiana_factory = ComidaItalianaFactory()
    bebida_ff = fast_food_factory.criar_bebida()
    prato_ff = fast_food_factory.criar_prato_principal()
    bebida_italiana = italiana_factory.criar_bebida()
    prato_italiano = italiana_factory.criar_prato_principal()
    print(fast_food_factory.criar_prato_principal().detalhes())
    print(italiana_factory.criar_bebida().detalhes())

    # 3. Builder
    print("\n=== Builder ===")
    builder = PedidoBuilder()
    pedido_personalizado = (
        builder.adicionar_item("Pizza")
        .adicionar_item("Refrigerante")
        .adicionar_acompanhamento("Molho extra")
        .construir()
    )
    print(pedido_personalizado)

    # 4. Adapter
    print("\n=== Adapter ===")
    sistema_legado = SistemaPagamento()
    sistema_novo = NovoSistemaPagamento()
    adaptador = PagamentoAdapter(sistema_novo)
    print("Usando sistema legado:")
    sistema_legado.processar_pagamento(50)
    print("Usando sistema novo com adaptador:")
    adaptador.processar_pagamento(50)

    # 5. Bridge
    print("\n=== Bridge ===")
    pedido_retirada = PedidoEntrega(Retirada())
    pedido_delivery = PedidoEntrega(Delivery())
    print("Método de entrega - Retirada:")
    pedido_retirada.processar_entrega()
    print("Método de entrega - Delivery:")
    pedido_delivery.processar_entrega()

    # 6. Composite
    print("\n=== Composite ===")
    categoria_pizzas = Categoria("Pizzas")
    categoria_pizzas.adicionar(Item("Margherita"))
    categoria_pizzas.adicionar(Item("Pepperoni"))
    categoria_bebidas = Categoria("Bebidas")
    categoria_bebidas.adicionar(Item("Refrigerante"))
    categoria_bebidas.adicionar(Item("Água"))
    print("Menu:")
    categoria_pizzas.exibir()
    categoria_bebidas.exibir()

    # 7. Chain of Responsibility
    print("\n=== Chain of Responsibility ===")
    handler_novo = NovoHandler()
    handler_preparacao = PreparacaoHandler(handler_novo)
    handler_pronto = ProntoHandler(handler_preparacao)
    pedido = type("Pedido", (), {"status": "novo"})  # Mock do pedido
    handler_pronto.handle(pedido)

    pedido.status = "em preparação"
    handler_pronto.handle(pedido)

    pedido.status = "pronto"
    handler_pronto.handle(pedido)

    # 8. State
    print("\n=== State ===")
    pedido_estado = PedidoEstado()
    pedido_estado.avancar()
    pedido_estado.avancar()
    pedido_estado.avancar()


if __name__ == "__main__":
    main()
