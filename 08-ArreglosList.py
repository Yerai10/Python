lenguajes =[ "Python", "Kotlin", "Java", "JavaScript"]
print (lenguajes) 

#Si elegimos la posición 0 devolvería Python
print ( lenguajes [0]) 
print ( lenguajes [2]) 


lenguajes.sort() #.sort ordena alfabeticamente
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[3]} "
print(aprendiendo)

#Modificar valores de un list
lenguajes [2] = "Php"
print (lenguajes)

#Agregar elementos a un arreglo
lenguajes.append("Ruby")
print(lenguajes)

#Eliminar un producto de un list
del lenguajes[1]
print (lenguajes)

#Eliminar un arreglo eliminando el ultimo elemento
lenguajes.pop()
print (lenguajes)

#eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre de un list
lenguajes.remove('Python')
print(lenguajes)



