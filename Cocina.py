class Cocina:
    def __init__(self, nombre, filo, vida):
        self.nombre = nombre
        self.filo = filo
        self.vida = vida
    def atributos(self):
        print("objeto =", self.nombre)
        print("filo =", self.filo)
        print("vida =", self.vida)
    def verificacion(self, olla, cebolla, tomate, pasta, agua):
        if olla and cebolla and tomate and pasta and agua:
            print("Todos los objetos están presentes.")
            print("Menu de Accion disponible.")
        else:
            print("Faltan objetos. No se puede iniciar.")
    def daño(self, vegetal):
        return 20
    def atacar(self, vegetal):
        if self.filo > 0:
            daño = self.daño(vegetal)
            vegetal.vida = vegetal.vida - daño
            self.filo = self.filo - 10
            print(self.nombre, "ha cortado a", vegetal.nombre)
            print("Vida de", vegetal.nombre, "=", vegetal.vida)
            print("Filo restante =", self.filo)
        else:
            print("El cuchillo esta inutil. Debes afilar.")
    def esta_inutil(self):
        return self.filo <= 0
    def afilar(self):
        self.filo = 100
        print("El cuchillo fue afilado. Filo al 100%")
    def ensamblar(self):
        print("Ingredientes procesados.")
        print("Colocando ingredientes en la olla")
    def hervir(self):
        while self.vida < 100:
            decision = input("¿Deseas seguir hirviendo? (si/no): ")
            if decision == "si":
                self.vida = self.vida + 20
                if self.vida > 100:
                    self.vida = 100
                print("Nivel de coccion =", self.vida)
            else:
                print("La coccion se detuvo.")
                break
    def servir(self):
        if self.vida == 100:
            print("Combate culinario finalizado")
            print("La pasta ha sido servida con exito ")
        else:
            print("La pasta aun no esta lista.")




cuchillo = Cocina("Cuchillo", 100, 0)
cebolla = Cocina("Cebolla", 0, 100)
tomate = Cocina("Tomate", 0, 100)
pasta = Cocina("Pastas", 0, 0)
cuchillo.verificacion(True, True, True, True, True)
cuchillo.atacar(cebolla)
cuchillo.atacar(tomate)
if cuchillo.esta_inutil():
    cuchillo.afilar()
cuchillo.ensamblar()
pasta.hervir()
pasta.servir()

