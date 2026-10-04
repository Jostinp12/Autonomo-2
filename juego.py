#escogemos la palabra que vamos a adivinar
palabra_secreta = "perro"
#escogemos el numero de intentos que vamos a tener
intentos = 3
#creamos una variable par contar cauntas letras adivino correctamente
aciertos = 0

#Escribimos el mensaje de Bienvenida al juego
print("Bienvenido al juego del ahorcado")
#Escribimos el mensaje de numero de intentos que tiene el jugador
print("tienes tres intentos para adivinar la palabra")

#Agregamos while para repetir el juego mientas el numero de intentos no sea 0
while intentos > 0:
        print("intentos restantes:", intentos)

        #Le pedimos al jugador que ingrese una letra
        letra = input("ingrese una letra: ")

        #Comprobamos si la letra ingresada esta en la palabra secreta
        if letra in palabra_secreta:
            print("la letra esta en la palabra")
            #contamos cuantas veces aparece la letra ingresada en la palabra secreta            
            aciertos = aciertos + palabra_secreta.count(letra)
        else:
            print("la letra no esta en la palabra")
            intentos = intentos - 1
            print(intentos, "intentos restantes")

         #comprobamos si ya acerto todas las letras de la palabra secreta
        if aciertos == len(palabra_secreta):
             print("has adivinado la palabra")
             break


#Si el numero de intentos es 0 entonces terminamos el juego
if intentos == 0:
 print("has perdido")