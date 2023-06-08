class Restaurante:
    
    def agregar_restaurante(self, nombre):
        self.nombre = nombre #Atributo
       

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}')

#Instanciar la clase
restaurante = Restaurante()
restaurante.agregar_restaurante("Pizzeria Mexico")
restaurante.mostrar_informacion()

restaurante2 = Restaurante()
restaurante2.agregar_restaurante("Hamburguesas Python")
restaurante2.mostrar_informacion()

#Mostrar informacion 
print(f' Nombre restaurante: {restaurante.nombre}')
print(f' Nombre restaurante: {restaurante2.nombre}')