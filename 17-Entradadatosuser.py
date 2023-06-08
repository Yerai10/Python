nombre = input("¿Cual es tu nombre:?  \r\n ")
print(f"Hola {nombre}")

#leer datos que serán numeros

edad = input("¿Cual es tu edad?: \r\n")

#Convertir edad string a entero
edad = int(edad)

if edad >= 18:
    print("Ya puedes votar")
else:
    print("No puede votar. Aún eres menor de edad")

    #Juego para mezclar con operadores
numero = input ("Agrega un numero y te diré si es par o impar \r\n")
numero = int (numero)

if numero % 2 == 0:
    print (f" El {numero} es par")
else:
    print(f" El {numero} es impar")