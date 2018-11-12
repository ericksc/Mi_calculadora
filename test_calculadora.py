from calculadora import operacion

def test_suma():
    tipo_operacion = 's'
    numero1 = 2
    numero2 = 1
    resultado = operacion.get(tipo_operacion, None)(numero1,
                                                    numero2)
    #Probar si la funcion sumar puede sumar 2+1
    assert  3 == resultado


def test_resta():
    tipo_operacion = 'r'
    numero1 = 2
    numero2 = 1
    resultado = operacion.get(tipo_operacion, None)(numero1,
                                                    numero2)
    #Probar si la funcion restar puede restar 2-1
    assert  1 == resultado

def test_multiplicar():
    tipo_operacion = 'm'
    numero1 = 2
    numero2 = 1
    resultado = operacion.get(tipo_operacion, None)(numero1,
                                                    numero2)
    #Probar si la funcion multiplicar puede multiplicar 2*1
    assert 2 == resultado

def test_dividir_entre_cero():
    tipo_operacion = 'd'
    numero1 = 2
    numero2 = 0
    resultado = operacion.get(tipo_operacion, None)(numero1,
                                                    numero2)
    #Probar si la funcion dividir puede tratar el caso
    #  division entre cero ejemplo 2/0
    # La funcion dividir retorna None
    assert None == resultado

def test_dividir():
    tipo_operacion = 'd'
    numero1 = 2
    numero2 = 2
    resultado = operacion.get(tipo_operacion, None)(numero1,
                                                    numero2)
    #Probar si la funcion dividir puede dividir 2/2
    assert 1 == resultado