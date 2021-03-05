def check_char(arg):  # recibe un argumento y evalua si es un caracter
    ESIZE = "Error: ESIZE: muchos elementos."  # error si hay mas de 1 elemento
    EALPHA = "Error: EALPHA : no en el alfabeto."  # error si arg no son letras
    EINVAL = "Error: EINVAL: argumento inválido."  # error si arg no es un char
    if isinstance(arg, str) is True:  # evalua que el argumento sea un str
        if arg.isalpha() is True:  # evalua que dentro de ese Str, haya letras
            if len(arg) == 1:  # evalua que elementos en arg sea 1
                return 0  # salida sera 0 si todo esto se cumple
            else:
                return ESIZE  # salida: error ESIZE si hay mas de 1 en arg
        else:
            return EALPHA  # salida: error EALPHA si en arg no solo hay letras
    else:
        return EINVAL  # salida: error EINVAL si el arg no es string


def caps_switch(arg):  # funcoion: toma el argumento que recibe Cher_char
    if check_char(arg) == 0:  # evalua si la salida de Check_Char es 0
        return arg.swapcase()  # si es asi, cambia Mayus a minus y viceversa
