# Agenda de contactos

import os

CARPETA = 'Contactos/'  # Carpeta de contactos
EXTENSION = '.txt'  # Extensión de archivos

# Contactos


class Contactos:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menu de opciones
    mostrar_menu()

    # Preguntar al usuario la accion a realizar con while
    preguntar = True
    while preguntar:
        opcion = input(' Seleccione una opción: \r\n')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False

        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contactos()
            preguntar = False
        elif opcion == 5:
            eliminar_contactos()
            preguntar = False
        else:
            print('  Opción no valida, intente de nuevo... ')

def eliminar_contactos():
    nombre = input(' Seleccione el Contacto que desea eliminar: \r\n')
    
    try:
        os.remove(CARPETA + nombre + EXTENSION)
    except:
        print( ' No existe ese contacto')


  
     # Reinicia la app
    app()
 
def buscar_contactos():
    nombre = input(' Seleccione el Contacto que desea buscar: \r\n')
    
    try:
        with open (CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del Contacto: \r\n')
            for    linea in contacto:
                print(linea.rsplit())
            print('\r\n')
    except IOError:
        print(' El archivo no existe ')
        print(IOError)

    #Reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    # Solo los que terminan en la extensión txt
    archivos_txt = [i for i in archivos if  i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open (CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos            
                print(linea.rsplit())

                # Imprime el separador
            print('r\n')


def editar_contacto():
    print('ESCRIBE GUAY')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            nombre_contacto = input(' Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input(' Agrega el Nuevo numero de telefono: \r\n')
            categoria_contacto = input(' Agrega la Nueva categoria: \r\n')
        #Instanciar

            contacto = Contactos(nombre_contacto, telefono_contacto, categoria_contacto)
        # Escribir en el arichivo

            archivo.write(' Nombre' + contacto.nombre + "\r\n")
            archivo.write(' Teléfono' + contacto.telefono + "\r\n")
            archivo.write(' Categoria' + contacto.categoria + "\r\n")
        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        # Mostrar mensaje de exito 

        print (' \r\n Contacto editado correctamente \r \n ' )
    else:
        print('Ese contacto no existe')

    # Reiniciar la app
    app()


def agregar_contacto():
    print(' Escribe los datos del nuevo contacto: ')
    nombre_contacto = input(' Nombre del contacto: \r\n')
    # Revisar si el archivo ya existe antes de crearlo isfile
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Resto de los campos
            telefono_contacto = input(' Agrega el numero de telefono: \r\n')
            categoria_contacto = input(' Agrega categoria: \r\n')
            # Instanciamos la clase
            contacto = Contactos(
                nombre_contacto, telefono_contacto, categoria_contacto)
            # Escribir en el archivo
            archivo.write(' Nombre' + contacto.nombre + "\r\n")
            archivo.write(' Teléfono' + contacto.telefono + "\r\n")
            archivo.write(' Categoria' + contacto.categoria + "\r\n")

            # Mostrar un mensaje de éxito
        print(' Contacto creado correctamente \r\n ')
    else:
        print('Ese contacto ya exite')

        # Reiniciar la app ()
        app()
    # Hasta aqui la primera opción agregar contacto


def mostrar_menu():
    print(' Seleccione del Menú lo que desee hacer: ')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')


def crear_directorio():
    '''
    test
    '''
    if not os.path.exists('Contactos/'):
        # Crear la carpeta
        os.makedirs('Contactos/')

    else:
        print('La carpeta ya existe')


def existe_contacto(nombre):
    '''
    test
    '''
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()
