class Calculadora:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        sumar = (self.numero1 + self.numero2)
        return round(sumar, 2)

    def resta(self):
        res = (self.numero1 - self.numero2)
        return round(res, 2)

    def multiplicacion(self):
        mul = self.numero1 * self.numero2
        return mul

    def division(self):
        if self.numero2 == 0: return 0
        div = (self.numero1 / self.numero2)
        return round(div, 2)
