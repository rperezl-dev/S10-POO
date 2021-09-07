class Basico:
    def numeros_n(self, n=10):
        print('Numeros del 1 al', n)
        for i in range(1, n+1):
            if i == n:
                print(str(i) + '.')
            else: print(str(i) + ', ' ,end='')

    def multiplo(self, numero=36):
        print('Multiplos de', numero, '\n0, ', end='')
        for i in range(1, numero+1):
            if (numero * i) % i == 0:
                if i == numero:
                    print(str(i*numero) + '.')
                else: print(str(i*numero) + ', ' ,end='')

    def divisores_numeros(self, numero=42):
        print('Divisores de', numero)
        for i in range(1, numero+1):
            if numero % i == 0:
                if i == numero:
                    print(str(i) + '.')
                else: print(str(i) + ', ' ,end='')

    def primo(self, numero=7):
        primo = False
        print('Número primo')
        if numero >= 2:
            for i in range(2, numero):
                if numero % i == 0:
                    print(' -No es primo')
                    primo = True
                    break
            if not primo:
                print(' -Es primo')
        else:
            print(' -No es primo')

    def perfecto(self, numero=6):
        print('Número perfecto')
        sum = 0
        for i in range(1, numero):
            if numero % i == 0:
                sum += i
        if numero == sum:
            print(' -El número es perfecto')
        else:
            print(' -El número no es perfecto')
