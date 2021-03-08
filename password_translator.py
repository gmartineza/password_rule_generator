import password_generator as gen
abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def interfaz_usuario():
    global abc_encriptado
    ui_abc_encriptado = input(
            "Opciones:\n"+
	    "1. No tengo un abecedario encriptado (generar uno).\n"+
	    "2. Ya tengo uno (usarlo).\n"+
	    "--> ")
    if ui_abc_encriptado.lower() == "1":
        abc_encriptado = gen.generador()
        print(abc_encriptado)
        pass
    elif ui_abc_encriptado.lower() == "2":
        abc_encriptado = input("Introduce tu abecedario encriptado\n--> ")
        pass
    traductor_antiguo()
def traductor_antiguo():
    entrada = input("Escribí lo que hay que encriptar\n--> ")
    transtable = entrada.maketrans(abc, abc_encriptado)
    print(entrada.translate(transtable))	

interfaz_usuario()
