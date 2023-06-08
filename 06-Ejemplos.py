def mensaje_Bienvenida ( mensaje):
    print( mensaje)

mensaje_Bienvenida( "Bienvendios al mundo de la Programación")

def informacion( nombre, apellidos = "", mensaje1= ""):
    print ( f"soy {nombre} {apellidos} y quiero darte un mensaje {mensaje1}")
    print ( f"soy {nombre} y quiero darte un mensaje {mensaje1}")


informacion( "Yerai", "Caballero Martin", " Bienvendios al mundo de la Programación" )

informacion( "Yerai", " Bienvendios al mundo de la Programación")