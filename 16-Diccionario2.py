#Iniciar un diccionario vacio
jugador = {}
print(jugador)

#Se une un jugador
jugador ["nombre"] = "Yerai"
jugador["puntuacion"]= 0
print(jugador)

#Incrementando la puntuacion 
jugador["puntuacion"]= 100
print(jugador)

#Acceder a un valor

print (jugador.get("consola", "no existe ese valor"))

#Iterar en el diccionario
for llave, valor in jugador.items():
    print (llave)
    print (valor)

# Para eliminar el jugador y la puntuacion
del jugador ["nombre"]
del jugador["puntuacion"] 
print(jugador)