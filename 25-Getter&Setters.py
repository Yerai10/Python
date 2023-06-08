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

#Instanciar la clase
restaurante = Restaurante( 'Pizzeria Mexico', 'Comida italiana', 50)

#restaurante.__precio = 80
restaurante.mostrar_informacion()
restaurante.get_precio()
restaurante.set_precio()


restaurante2 = Restaurante('Pizzeria España', 'Comida española', 20)

#restaurante.__precio= 50
restaurante2.mostrar_informacion()
restaurante2.get_precio()
restaurante2.set_precio()

