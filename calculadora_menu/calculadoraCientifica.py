from .calculadora import Calculadora


class calCientifica(Calculadora):
    PI = 3.1416

    def __init__(self, numero1=0, numero2=0):
        super().__init__()
    
    def circunferencia(self, radio):
        circu = (2 * self.PI) * radio
        return round(circu, 2)

    def areaCirculo(self, radio):
        a_cir = (self.PI * (radio**2))
        return round(a_cir, 2)

    def areaCuadrado(self, lado):
        a_cuad = (lado * lado)
        return round(a_cuad, 2)
