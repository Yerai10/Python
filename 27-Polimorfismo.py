class Restaurante:

    def __init__(self,nombre, categoria, precio):
       self.nombre = nombre
       self.categoria = categoria #Default están en public
       self.precio = precio  #con protected se pondría con _ Luego esta PRIVATE con __ (dos guiones bajos) y lo midifcariamos con un get oset 

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, {self.categoria}, Precio: {self.precio}')


#Getters - Get obtiene un valor de una clase Private
    def get_precio(self):
        print(self.precio)
#Setters - Set agrega un valor de una clase Private

    def set_precio(self):
        print(self.precio)

#Polimorfismo : Crear una clase hijo de Restaurante pero con más argumentos o menos (piscina)
class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, piscina, oferta):
        super().__init__(nombre, categoria, precio)
        self.piscina = piscina
        self.oferta = oferta
#Tambien puedes agregar un metodo que solo exista en Hotel (oferta)

    def get_oferta (self):
        return self.oferta
    
#También otra forma de polimorfismo sería rescribir un método (debe llamarse igual) con diferente info
    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, {self.categoria}, Precio: {self.precio}, Oferta: {self.oferta}')


hotel = Hotel("Hotel AR", "5 Estrellas", 200, " " ,"Si hay oferta")
hotel.mostrar_informacion()
oferta = hotel.get_oferta()
print(oferta)

