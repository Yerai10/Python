examen = "Bienvenido al examen"
print (examen)

# Para incrementar de uno en uno 
numero0 = 0
numero1 = 0
print( f" Tu puntuacion es {numero0}")

#Primera pregunta

pregunta1 = input("¿El color mas oscuro que existe es el negro? \r\n" )
numero1 += 1
numero0 = 0
if pregunta1 == "SI":
    print (f" Respuesta correcta, tu puntuacion es {numero1}")

else:
    print(f"Respuesta incorrecta, tu puntuacion es {numero0}")

#Segunda pregunta
pregunta2 = input("¿El color mas claro que existe es el negro? \r\n" )
numero1 +=1
numero0 += 0

if pregunta2 == "NO":
    print (f" Respuesta correcta, tu puntuacion es {numero1 + numero0}")
else: 
    print(f"Respuesta incorrecta, tu puntuacion es {numero0 - numero1}")

#Tercera pregunta:
pregunta3 = input("¿Cuando sale el sol hace calor? \r\n" )
numero1 += 1 
if pregunta3 == "SI":
    print (f" Respuesta correcta, tu puntuacion es {numero1 + numero0}")

else: 
    print(f"Respuesta incorrecta,  tu puntiacion es {numero0 - numero1}")

# Resultado
puntuacion = numero1 + numero0
print (f"Tu puntuación final es {puntuacion}")