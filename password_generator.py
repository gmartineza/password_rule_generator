import random as rnd

caracteres=[
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 

"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 

"1", "2", "3", "4", "5", "6", "7", "8", "9", "0",

"!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]

encriptado_final=""

def encriptor():
    global encriptado_final
    clave = rnd.choice(caracteres)
    if clave not in encriptado_final:
        encriptado_final += clave
    else:
        encriptor()

def generador():
    global encriptado_final
    for i in range(26*2):
        encriptor()
    return encriptado_final
