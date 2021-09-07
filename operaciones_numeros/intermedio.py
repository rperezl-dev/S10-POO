from .basico import Basico


class Intermedio(Basico):
    def numeros_n(self, n=10):
        print('Suma del número 1 al', n)
        suma = 0
        for i in range(1, n+1):
            suma += i
        print('La suma es igual a:', suma)

    def factorial(self, numero=5):
        print('Número factorial')
        facto = 1
        if numero != 0:
            for i in range(1, numero+1):
                facto *= i
        print('El factorial es:', facto)

    def fibonacci(self, n=20):
        print('Fibonacci hasta el', n, '\n' + '0')
        for i in range(n-1):
            a = 0
            b = 1
            for _ in range(i):
                c = a + b
                a = b
                b = c
            print(b)

    def primos_gemelos(self, num1=1, num2=10):
        if num1 != num2:
            a = 0
            b = 0
            if num1 > num2:
                n3 = num1
                num1 = num2
                num2 = n3
            print('Números primos gemelos del', num1, 'al', num2)
            if num2 > 4:
                for i in range(num1, num2+1):
                    incr = 2
                    primo = True
                    while primo and incr < i:
                        if i % incr == 0:
                            primo = False
                        else:
                            incr += 1
                    if primo and not a:
                        a = i
                    elif primo and a:
                        b = i
                        if b-a == 2:
                            print(a, 'y', b, 'son números primos gemelos.')
                        a = i
            else:
                print('No hay números gemelos.')
        else:
            print('Ingrese números diferentes')

    def amigos(self, num1=1184, num2=1210):
        if num1 != num2:
            print('Números amigos')
            suma_a, suma_b= 0, 0
            if num1 > num2:
                n3 = num1
                num1 = num2
                num2 = n3
            for cont in range(1, num1+1):
                if num1 % cont == 0:
                    suma_a += cont
            for cont in range(1, num2+1):
                if num2 % cont == 0:
                    suma_b += cont
            if suma_a == suma_b and suma_b == suma_a:
                print(' -Son amigos')
            else:
                print(' -No son amigos')
        else:
            print('Ingrese números diferentes')
