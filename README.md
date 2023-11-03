<img width="830" alt="image" src="https://github.com/MuchSquid/Testy/assets/41312479/b335f375-baa4-4153-a932-11b9bd0e7f9c"><img width="830" alt="image" src="https://github.com/MuchSquid/Testy/assets/41312479/e1ed04b2-c16e-45b2-8331-d0cf946427aa">
# Actividad EC2 - Refactorizacion

Integrantes:
- Esteban Andre Vasquez Grados
- Ximena Nicolle Lindo Peña
- Luis David Golac Córdova
- Sebastian Alonso Loza Mendoza
- Luis Méndez Lázaro

## Tecnicas Aplicadas:

Validación de entrada:

-Verificando el DNI antes de agregar los datos a la lista dentro del método leer_datos, se garantiza que solo se procesen datos válidos.

Uso de estructuras de datos eficientes:

- El uso de la clase Counter de la biblioteca collections para calcular el número de votos por candidato en el método calcular_ganador proporciona una manera eficiente y legible de contar elementos.

Manejo de excepciones:

- El manejo de excepciones en leer_datos con try...except previene la terminación abrupta del programa en caso de que el archivo CSV no se pueda abrir, mejorando la robustez del código.

Expresiones regulares:

- Utilizar expresiones regulares para validar el formato del DNI en el método dni_valido es una forma potente y flexible de realizar validaciones.

Pruebas unitarias:

- La inclusión de un conjunto de pruebas unitarias asegura que el código funcione como se espera. Esto facilita la detección de errores y problemas de lógica.

## Evaluacion del codigo resultante

![imagen1](https://media.discordapp.net/attachments/1092557833070981120/1169860412737585152/image.png?ex=6556f069&is=65447b69&hm=8c4403e5cc8d95ada452134a31667e3468b5265d12ec0217c2ffc056abb8a323&=&width=2566&height=998)
