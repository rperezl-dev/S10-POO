from os import system as pantalla_win
from calculadora_menu.calculadoraEstandar import calEstandar
from calculadora_menu.calculadoraCientifica import calCientifica


class CalculadorasMenu:
    def __init__(self):
        pass

    def menu(self):
        pantalla_win('cls')
        opc = 0
        calcu_cientifica = calCientifica()
        while opc != 10:
            print('+Menú Calculadora+')
            print('  1) Suma')
            print('  2) Resta')
            print('  3) Multiplicacion')
            print('  4) Division')
            print('  5) Exponente')
            print('  6) Valor Absoluto')
            print('  7) Circunferencia')
            print('  8) Area Circulo')
            print('  9) Area Cuadrado')
            print(' 10) Salir')
            print('********************\n')
            while True:
                try:
                    opc = int(input('Ingrese una opción: '))
                    if opc not in range(1, 11):
                        print('Ingrese una opción disponible.')
                    else:
                        break
                except ValueError:
                    print('Ingrese una opción válida.')
            print('')
            if opc != 10:
                if opc not in range(6, 10):
                    while True:
                        try:
                            num1 = float(input('Ingrese un número: '))
                            num2 = float(input('Ingrese otro número: '))
                            break
                        except ValueError:
                            print('Ingrese valores correctos.')
                    calcu_estandar = calEstandar(num1, num2)
                print('')
                if opc == 1:
                    print('La suma es igual a:', calcu_estandar.suma())
                elif opc == 2:
                    print('La resta es igual a:', calcu_estandar.resta())
                elif opc == 3:
                    print('La multiplicación es igual a:', calcu_estandar.multiplicacion())
                elif opc == 4:
                    print('La división es igual a:', calcu_estandar.division())
                elif opc == 5:
                    print('El número {} elevado al exponente {} es igual a: {}'.format(num1, num2, calcu_estandar.exponente()))
                elif opc == 6:
                    while True:
                        try:
                            num1 = float(input('Ingrese un número: '))
                            break
                        except ValueError:
                            print('Ingrese un valor correcto.')
                    print('\nEl valor absoluto es igual a:', calcu_estandar.valorAbsoluto(num1))
                else:  # OPCIONES 7, 8 y 9
                    if opc in range(7, 9):
                        while True:
                            try:
                                rad = float((input('Ingrese el radio: ')))
                                break
                            except ValueError:
                                print('Ingrese un valor correcto.')
                        if opc == 7:
                            print('La circunferencia es igual a:', calcu_cientifica.circunferencia(rad))
                        else:  # OPCION == 8
                            print('El área del circulo es igual a:', calcu_cientifica.areaCirculo(rad))
                    else:  # OPCION == 9
                        while True:
                            try:
                                lado = float((input('Ingrese un lado: ')))
                                break
                            except ValueError:
                                print('Ingrese un valor correcto.')
                        print('El área del cuadrado es igual a:', calcu_cientifica.areaCuadrado(lado))
            else:
                print('¡Gracias por visitarnos!')
            input('\nPulsa Enter <-- para salir... ')
            pantalla_win('cls')
