from cuchillo import Cuchillo
from ingredientes import Ingredientes
from tomate import Tomate
from cebolla import Cebolla
from pasta import Pasta
from agua import Agua
from olla import Olla
from cocina import cocina

def _init_(self):

        self.cuchillo = Cuchillo()
        self.tomate = Tomate()
        self.cebolla = Cebolla()
        self.agua = Agua()
        self.olla = Olla(self.agua)
        self.pasta = Pasta()
        self.cocina = cocina()


        while self.tomate.esta_vivo():
            self.cuchillo.cortar(self.tomate)

        while self.cebolla.esta_vivo():
            self.cuchillo.cortar(self.cebolla)

        print(" Cocinando pasta ")

        self.agua.hervir()
        self.olla.cocinar_pasta(self.pasta)

        print("Comida lista!")
        