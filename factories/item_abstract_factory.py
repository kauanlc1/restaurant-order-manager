from abc import ABC, abstractmethod


# Produtos base
class Bebida(ABC):
    @abstractmethod
    def detalhes(self):
        pass


class PratoPrincipal(ABC):
    @abstractmethod
    def detalhes(self):
        pass


# Produtos concretos
class Refrigerante(Bebida):
    def detalhes(self):
        return "Refrigerante gelado"


class Suco(Bebida):
    def detalhes(self):
        return "Suco natural"


class Pizza(PratoPrincipal):
    def detalhes(self):
        return "Pizza deliciosa"


class Massa(PratoPrincipal):
    def detalhes(self):
        return "Massa fresca"


# Abstract Factory
class ItemFactory(ABC):
    @abstractmethod
    def criar_bebida(self) -> Bebida:
        pass

    @abstractmethod
    def criar_prato_principal(self) -> PratoPrincipal:
        pass


# Factories concretas
class ComidaItalianaFactory(ItemFactory):
    def criar_bebida(self) -> Bebida:
        return Suco()

    def criar_prato_principal(self) -> PratoPrincipal:
        return Massa()


class ComidaFastFoodFactory(ItemFactory):
    def criar_bebida(self) -> Bebida:
        return Refrigerante()

    def criar_prato_principal(self) -> PratoPrincipal:
        return Pizza()
