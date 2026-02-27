class Agua:
    def _init_(self):
        self._temperatura = 25  # Encapsulado

    def hervir(self):
        self._temperatura = 100
        print("El agua está hirviendo a 100°C")