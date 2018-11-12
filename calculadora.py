#Esto es un programa ejemplo
# de implementacion de calculadora

def mensaje_inicial():
    print('Seleccione la operacion a realizar')

def pedir_datos():
    print('Ingresa la opcion:')
    print('suma=s'
          'resta=r'
          'multiplica=m'
          'divide=d'
          'salir=x')
    oper=  input('Opcion:')
    if oper == 'x':
        salir()
    n1 = float(input('Primer numero='))
    n2 = float(input('Segundo numero='))

    conversion = {'s': 'sumar',
         'r': 'restar',
         'm': 'multiplicar',
         'd': 'dividir'}
    resultado = operacion.get(oper, None)(n1,n2)
    if resultado is None:
        print(f'No hay resultado valido de {conversion[oper]} con numeros {n1} y {n2}')
    else:
        print(f'Resultado de {conversion[oper]} con numeros {n1} y {n2} es: {resultado}')

def no_mas_ciclo(*args):
    bandera = False

def salir():
    print('Saliendo de calculadora')
    import sys
    sys.exit()

def divide(x,y):
    try:
        resultado = x/y
    except ZeroDivisionError as e:
        resultado = None
    finally:
        return resultado

operacion = {
    's' : lambda x,y: x+y,
    'r':  lambda x,y: x-y,
    'm': lambda x,y: x*y,
    'd': divide,
    'x': no_mas_ciclo
}

if __name__ == "__main__":
    bandera = True
    while(bandera):
        mensaje_inicial()
        pedir_datos()

    salir()