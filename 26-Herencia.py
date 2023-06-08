class Restaurante:

    def __init__(self,nombre, categoria, precio):
       self.nombre = nombre
       self.categoria = categoria #Default están en public
       self.__precio = precio  #con protected se pondría con _ Luego esta PRIVATE con __ (dos guiones bajos) y lo midifcariamos con un get oset 

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, {self.categoria}, Precio: {self.__precio}')


#Getters - Get obtiene un valor de una clase Private
    def get_precio(self):
        print(self.__precio)
#Setters - Set agrega un valor de una clase Private

    def set_precio(self):
        print(self.__precio)

#Herencia : Crear una clase hijo de Restaurante
class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel("Hotel AR", "5 Estrellas", 200)
hotel.mostrar_informacion()