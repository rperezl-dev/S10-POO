from os import system as pantalla_win
from operaciones_numeros.basico import Basico
from operaciones_numeros.intermedio import Intermedio


class OperacionesConNumeros:
    def __init__(self):
        pass

    def menu(self):
        pantalla_win('cls')
        opc = 0
        ope_basica = Basico()
        ope_intermedia = Intermedio()
        while opc != 11:
            print('+Menú Operación Números+')
            print('  1) Presentar los números de 1 a n')
            print('  2) Sumar los números de 1 a n')
            print('  3) Múltiplo de cualquier numero')
            print('  4) Presentar los divisores de un numero')
            print('  5) Numero Primo')
            print('  6) Factorial de cualquier numero')
            print('  7) Fibonacci de una serie de n números')
            print('  8) Perfecto')
            print('  9) Primos gemelos')
            print(' 10) Números amigos')
            print(' 11) Salir')
            print('*****************************************\n')
            while True:
                try:
                    opc = int(input('Ingrese una opción: '))
                    if opc not in range(1, 12):
                        print('Ingrese una opción disponible.')
                    else:
                        break
                except ValueError:
                    print('Ingrese una opción válida.')
            print('')
            if opc != 11:
                if opc in range(1, 9):
                    while True:
                        try:
                            numero_uni = int(input('Ingrese un número: '))
                            if numero_uni > 0:
                                break
                            else:
                                print('Ingrese un número positivo mayor a 0.')
                        except ValueError:
                            print('Ingrese valores correctos.')
                else:
                    while True:
                        try:
                            num1 = int(input('Ingrese un número: '))
                            num2 = int(input('Ingrese otro número: '))
                            if num1 > 0 and num2 > 0:
                                break
                            else:
                                print('Ingrese un número positivo mayor a 0.')
                        except ValueError:
                            print('Ingrese valores correctos.')
                print('')
                if opc == 1:
                    ope_basica.numeros_n(numero_uni)
                elif opc == 2:
                    ope_intermedia.numeros_n(numero_uni)
                elif opc == 3:
                    ope_intermedia.multiplo(numero_uni)
                elif opc == 4:
                    ope_intermedia.divisores_numeros(numero_uni)
                elif opc == 5:
                    ope_intermedia.primo(numero_uni)
                elif opc == 6:
                    ope_intermedia.factorial(numero_uni)
                elif opc == 7:
                    ope_intermedia.fibonacci(numero_uni)
                elif opc == 8:
                    ope_intermedia.perfecto(numero_uni)
                elif opc == 9:
                    ope_intermedia.primos_gemelos(num1, num2)
                else:  # OPCION 10.
                    ope_intermedia.amigos(num1, num2)
            else:
                print('¡Gracias por visitarnos!')
            input('\nPulsa Enter <-- para salir... ')
            pantalla_win('cls')
            