# ERR 1x2 -6
# ERR2    -2.5


import tarea1_micros  # se importa el código para testear
ESIZE = "Error: ESIZE: muchos elementos."  # error si hay mas de 1 elemento
EALPHA = "Error: EALPHA : no en el alfabeto."  # error si arg no son letras
EINVAL = "Error: EINVAL: argumento inválido."  # error si arg no es un char


def test_check_char():  # función para testear que check_char funcione correctamente
    respuesta = tarea1_micros.check_char("A")  # guarda el valor de la salida de check_char en una variable con un argumento correcto
    assert respuesta == 0  # iguala esa variable al valor esperado de salida

def test_caps_switch():  # funcion para testear que caps_switch funcione correctamente
    evalu = tarea1_micros.caps_switch("a")  # guarda el valor de la salida de check_char en una variable con un argumento correcto
    assert evalu == "A"  # iguala esa salida con el valor esperado de la salida (mayus a mins o viceversa del argumento)

def test_caps_switch_b():  # funcion que va a evaluar que el error ESIZE se de correctamente
    errorb = tarea1_micros.check_char("abc")  # se evalua check_char con un argumento de mas de un elemento
    assert errorb == ESIZE  # se prueba que efectivamente el error salga

def test_caps_switch_c():  # funcion que va a evaluar que el error EALPHA se de correctamente
    errorc = tarea1_micros.check_char("1")  # se evalua check_char con un argumento que si sea string, pero no este entre A-Z
    assert errorc == EALPHA  # se prueba que efectivamente el error salga

def test_caps_switch_d():  # funcion que va a evaluar que el error EINVAL se de correctamente
    errord = tarea1_micros.check_char(4) # se evalua check_char con un argumento de tipo INT
    assert errord == EINVAL  # se prueba que efectivamente el error salga
