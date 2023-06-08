#Operadores and y or
#and - Revisa que se cumplan todas las condiciones
usuario_logeado = False
usuario_admin = False
if usuario_admin and usuario_logeado:
    print("Administrador")
elif usuario_logeado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")

#or - Revisa que se cumpla al menos 1 condicion

usuario_logeado = False
usuario_admin = True
if usuario_admin or usuario_logeado:
    print("Administrador")
elif usuario_logeado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")