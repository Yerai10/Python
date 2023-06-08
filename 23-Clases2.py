class Restaurante:

    def __init__(self,nombre, categoria, precio):
       self.nombre = nombre
       self.categoria = categoria
       self.precio = precio

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, {self.categoria}, Precio: {self.precio}')

#Instanciar la clase
restaurante = Restaurante( 'Pizzeria Mexico', 'Comida italiana', 50)
restaurante.mostrar_informacion()


restaurante2 = Restaurante('Pizzeria España', 'Comida española', 20)
restaurante2.mostrar_informacion()


