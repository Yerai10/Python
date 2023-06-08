#Creando un diccionario simple

cancion = { 
    "Artista": "Metalica",
    "Cancion": "Enter Sandman",
    "Lanzamiento": 1992,
    "likes": 25600
}
#Acceder a los elementos del diccionario

print(cancion ["Artista"])
print(cancion ["Lanzamiento"])

#Mezclar con un String asignariamos una variable
artista = cancion["Artista"]
print(f"Estoy escuchanndo {artista}")

#Agregar nuevos valores
cancion ["Playlist"] = "Heavy Metal"
print(cancion)

#Remplazar valor existente
cancion ["Cancion"] = "Seek & Destroy"
print(cancion)

#Para eliminar un valor existente
del cancion ["Lanzamiento"]
print(cancion)