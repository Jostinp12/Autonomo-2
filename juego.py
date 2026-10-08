import random  

#1. agregamos una lista con palabras de ciberseguridad que se va a adivinar
palabra_secreta = ["firewall", "phishing", "malware", "router", "algoritmo", "cifrado"]

#2. agregamos random.choice para escoger una palabra al azar de la lista
palabra_secreta = random.choice(palabra_secreta)   

#3. agregamos una lista con guiones bajos (_) por cada letra que tenga la palabra secreta
palabra_oculta = ["_"] * len(palabra_secreta)

#4. escogemos el numero de intentos que vamos a tener
intentos = 6

#Escribimos el mensaje de Bienvenida al juego
print("Bienvenido al juego del ahorcado")
#Escribimos el mensaje de numero de intentos que tiene el jugador
print("tienes seis intentos para adivinar la palabra")

#Agregamos while para repetir el juego mientas el numero de intentos no sea 0
while intentos > 0:
#Mostramos el estado actual de la palabra oculta unida por espacios (ej. _ i _ _ w a _ _ )
        print("\nPalabra:", " ".join(palabra_oculta))
        print("intentos restantes:", intentos)

        #Le pedimos al jugador que ingrese una letra
        letra = input("ingrese una letra: ")

        #Comprobamos si la letra ingresada esta en la palabra secreta
        if letra in palabra_secreta:
            print("la letra esta en la palabra")
            #recorremos la palabra para descubrir la letra en las posiciones que coincidan
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra
        else:
            print("la letra no esta en la palabra")
            intentos = intentos - 1
            print(intentos, "intentos restantes")

         #comprobamos si ya acerto no quedan guiones bajos (es decir, adivinó todas las letras)
        if "_" not in palabra_oculta:
             print("\n¡Has adivinado la palabra completa:", palabra_secreta, "!")
             break


#Si el numero de intentos es 0 entonces terminamos el juego
if intentos == 0:
 print("has perdido")