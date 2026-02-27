class Ingredientes:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self._vida = vida # Encapsulamiento (atributo protegido)

    def recibir_corte(self, daño):
        self._vida -= daño
        if self._vida < 0:
            self._vida = 0
        print(f"{self.nombre} tiene {self._vida}% de vida")

    def esta_vivo(self):
        return self._vida > 0