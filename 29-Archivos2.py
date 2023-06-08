#con With open no es necesario cerrar el archivo ya que se cierra automaticamente 
# r lee pero podriamos no pasarlo porque por default lee 
# .rstrip() es um metodo para eliminar en el print los saltos de linea
def app():

    with open('archivo.txt', "r") as archivo: 
        for contenido in archivo:
            print(contenido.rstrip())

app()