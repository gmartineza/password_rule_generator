import random as rnd

abecedario=[
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

encriptado=[
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 

"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 

"1", "2", "3", "4", "5", "6", "7", "8", "9", "0",

"!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]

encriptado_final=[]

def encriptor():
	clave= rnd.choice(encriptado)
	if clave not in encriptado_final:
		encriptado_final.append(clave)
	else:
		encriptor()

for letras in enumerate(abecedario):
	index=letras[0]
	encriptor()
	print(abecedario[index], ":", encriptado_final[index])
