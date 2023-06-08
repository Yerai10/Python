#Evaluar si existe un elemento en una lista
lenguajes = ["Python", "PHP", "Java", "JavaScript", "Kotlin"]
if "PHP" in lenguajes:
    print("PHP si existe")
else:
    print ("No existe este lenguaje")

#If anidados
usuario_autenticado = False
usuario_admin = False
if usuario_autenticado:
    if usuario_admin:
        print("Acesso total")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesion")