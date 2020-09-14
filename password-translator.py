abecedario=	"abcdefghijklmnopqrstuvwxyz"
encriptado= "o:.h=4+BNUnbqH!>fV&7Mp6DSX"

def interfaz_usuario():
	ui_abc_encriptado = input(
		"¿Quiere generar un abecedario encriptado? (Si ya tiene uno ponga N)"+
		"\nN/S-> ")
	if ui_abc_encriptado.lower() == s:
		

def traductor():
	entrada = input("escribí lo que hay que encriptar\n-> ")
	
	transtable = entrada.maketrans(abecedario, encriptado)
	
	print(entrada.translate(transtable))	

traductor()
