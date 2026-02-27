class Cuchillo:
    def _init_(self):
        self._filo = 30   # Encapsulamiento

    def cortar(self, ingrediente):
        if self._filo > 0:
            print("El cuchillo corta ")
            ingrediente.recibir_corte(10)
            self._filo -= 5
            print(f"El cuchillo ahora tiene {self._filo} de filo")
        else:
            print("El cuchillo no tiene filo ")
