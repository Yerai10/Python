class Restaurante:

    def __init__(self,nombre, categoria, precio):
       self.nombre = nombre
       self.categoria = categoria #Default están en public
       self._precio = precio  #con protected se pondría con _ Luego esta PRIVATE con __ (dos guiones bajos) y lo midifcariamos con un get oset 

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, {self.categoria}, Precio: {self._precio}')

#Instanciar la clase
restaurante = Restaurante( 'Pizzeria Mexico', 'Comida italiana', 50)
print(restaurante._precio)
restaurante._precio = 80
restaurante.mostrar_informacion()


restaurante2 = Restaurante('Pizzeria España', 'Comida española', 20)
print(restaurante2._precio)
restaurante._precio= 50
restaurante2.mostrar_informacion()


