from os import system as pantalla_win


class OperacionesConCadenas:
    def __init__(self, cadena=''):
        self.cadena = cadena
    
    def recorrerCadena(self):
        for i in self.cadena:
            print(i)
    
    def buscarCaracter(self, buscado=''):
        caracter_encontrado = self.cadena.find(buscado)
        if caracter_encontrado > 0:
            print('El caracter {} consta dentro de la cadena.'.format(buscado))
        else:
            print('El caracter {} no consta en la cadena.'.format(buscado))

    def listaPosiciones(self, caracter=''):
        lta_posiciones = []
        for i in range(0, len(self.cadena)):
            if self.cadena[i].lower() == caracter:
                lta_posiciones.append(i+1)
        return lta_posiciones

    def listaPalabras(self):
        while True:
            if len(self.cadena)+1 > 1:
                break
            else:
                print('Ingrese una palabra válida.')
                self.cadena = input('Ingrese una palabra: ').lower().replace(' ', '')
        return list(self.cadena.split())

    def cadenaLista(self):
        print('Ingreso de elementos')
        print('Ingrese -- para salir')
        lta_conversion = []
        while True:
            conv_caracter = input('Ingrese caracteres: ')
            if conv_caracter.replace(' ', '') == '--':
                break
            lta_conversion.append(conv_caracter)
        conv_cadena = ''.join(lta_conversion)
        print('Lista:', lta_conversion)
        print('Cadena:', conv_cadena)
    
    def insertarDato(self, buscado, posicion):
        cadena = list(self.cadena)
        cadena.insert(posicion, buscado)
        conversion_string = ''.join(cadena)
        print('Cadena nueva:', conversion_string)
    
    def eliminarOcurrencias(self, buscado):
        print('Cadena nueva:', self.cadena.lower().replace(buscado, ''))

    def retornaValor(self, posicion):
        cadena = list(self.cadena)
        vueltas = 0
        for i in posicion:
            if vueltas > 0:
                cadena.pop((i-1)-vueltas)
            else:
                cadena.pop(i-1)
            vueltas += 1
        return ''.join(cadena)
    
    def concatenarCadena(self, dato):
        print('Cadena concatenada:', self.cadena + dato)


def menu():
    pantalla_win('cls')
    cadena = ''
    opc = 0
    while opc != 10:
        print('+Menú Operaciones de Cadenas+')
        print('  1) Recorrer y presentar los datos de una cadena')
        print('  2) Buscar un carácter en una cadena')
        print('  3) Retornar una lista con la posiciones dado un carácter de la cadena')
        print('  4) Retornar una lista con todas las palabras de una cadena')
        print('  5) Retornar una cadena a partir de una lista')
        print('  6) Insertar un dato en una cadena dada lo Posición')
        print('  7) Eliminar todas las ocurrencias en una cadena')
        print('  8) Retornar cualquier valor de una cadena eliminándolo ')
        print('  9) Concatenar cadenas')
        print(' 10) Salir')
        print('************************************************************************\n')
        while True:
            try:
                opc = int(input('Ingrese una opción: '))
                if opc not in range(1, 11):
                    print('Ingrese un opción disponible.')
                else:
                    break
            except ValueError:
                print('Ingrese una opción válida.')    
        if opc != 10:
            if opc != 5:
                cadena_str = input('\nIngrese una cadena: ')
            cadena = OperacionesConCadenas(cadena_str)
            if opc == 1:
                print('')
                cadena.recorrerCadena()
            elif opc == 2:
                print('')
                while True:
                    buscar_caracter = input('Ingrese el caracter a buscar: ').lower().replace(' ', '')
                    if len(buscar_caracter) > 0 and len(buscar_caracter) < 2:
                        break
                    else:
                        print('Ingrese un caracter válido.')
                cadena.buscarCaracter(buscar_caracter)
            elif opc == 3:
                print('')
                while True:
                    listar_caracter = input('Ingrese el caracter a ser listado: ').lower().replace(' ', '')
                    if len(listar_caracter) > 0 and len(listar_caracter) < 2:
                        break
                    else:
                        print('Ingrese un caracter válido.')
                lta_caracter_posicion = cadena.listaPosiciones(listar_caracter)
                print('Posiciones encontradas: {}'.format(lta_caracter_posicion))
            elif opc == 4:
                print('')
                lta_palabra_posicion = cadena.listaPalabras()
                print('Posiciones encontradas: {}'.format(lta_palabra_posicion))
            elif opc == 5:
                print('')
                cadena.cadenaLista()
            elif opc == 6:
                print('')
                insertar_dato = input('Ingrese un dato a insertar: ')
                while True:
                    try:
                        insertar_posicion = int(input('Del número 1 al {} ingrese la posición: '.format(len(cadena_str))))
                        if insertar_posicion in range(1, len(cadena_str)+1):
                            break
                        else: print('Ingrese una posición correcta.')
                    except ValueError:
                        print('Ingrese un valor correcto.')
                cadena.insertarDato(insertar_dato, insertar_posicion)
            elif opc == 7:
                print('')
                ocurrencia = input('Ingrese los caracteres a eliminar: ').lower()
                cadena.eliminarOcurrencias(ocurrencia)
            elif opc == 8:
                print('')
                print('Ingreso de posiciones')
                print('Pulsar -- para salir')
                posiciones = set()
                while True:
                    pos = input('Del número 1 al {} ingrese las posiciones a eliminar: '.format(len(cadena_str)))
                    if pos.replace(' ', '') == '--':
                        break
                    try:
                        pos = int(pos)
                        if pos in range(1, len(cadena_str)+1):
                            posiciones.add(pos)
                        else: print('Ingrese una posición correcta.')
                    except ValueError:
                        print('Ingrese valores válidos.')
                nuevo_valor = cadena.retornaValor(posiciones)
                print('Cadena nueva retornada:', nuevo_valor)
            else:
                print('')
                cadena_concatenar = input('Ingrese otra cadena: ')
                cadena.concatenarCadena(cadena_concatenar)
        else: print('\n¡Gracias por visitarnos!')
        input('\nPulsa Enter <-- para salir... ')
        pantalla_win('cls')
