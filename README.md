# Proyecto Integrador: Juego del Ahorcado en Python
**Asignatura:** Lógica de Programación  
**Estudiante:** Jostin Alexander Cuaspa Calle  
**Institución:** Universidad Internacional del Ecuador (UIDE)  

---

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de una versión interactiva del clásico **juego del ahorcado** implementada en **Python**, orientada a reforzar conceptos clave de la lógica de programación.

## Características Técnicas
* **Selección Aleatoria:** Utiliza la librería `random` junto con la función `random.choice()` para escoger una palabra secreta de forma aleaotria de la lkista de palabras.
* **Manejo de Estructuras de Datos:** Almacena las palabras en una **lista** y las cambia por guiones bajos (`_`) para representar la posición de cada letra en la palabra secreta.
* **Control de Flujo:** 
  * Bucle `while` para mantener el juego activo turno tras turno.
  * Bucle `for` y condicionales `if/else` para validar las letras ingresadas, descubrir las letras acertadas y restar intentos en caso de fallo.

