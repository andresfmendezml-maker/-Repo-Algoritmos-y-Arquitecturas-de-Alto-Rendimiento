entrada = input("Introduzca el numero a invertir")
salida = ""

for i in range(len(entrada)) : #len es para analizar la posicion de cada letra de la cadena de caracteres
    salida = entrada[i] + salida #Suma por la derecha para invertir el numero
print(salida)