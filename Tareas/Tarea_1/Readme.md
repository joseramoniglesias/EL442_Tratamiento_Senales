# Trabajo a Realizar 01: ¿Qué hora es?

## Enunciado

El objetivo de esta tarea es realizar un programa individual que determine automáticamente la hora que indica un reloj. En esta [carpeta](https://github.com/joseramoniglesias/Tratamiento_Senales/tree/main/Tareas/Tarea_1/Im%C3%A1genes) se encuentran 6 fotografías del reloj, que deben ser leídas por un programa y datos para determinar para automáticamente qué hora es, tal y como se muestra en este ejemplo para la primera imagen.

![image](https://user-images.githubusercontent.com/38440709/224081127-537de51b-d96d-4ccd-909f-abad9dcc033a.png)


Se debe realizar un programa que i) el reloj en la imagen (es necesario segmentarlo del fondo y del marco), ii) realizar una corrección geométrica para que el reloj se vea como un círculo, iii) encontrar las dos manecillas (para la hora y los minutos) iv) estime el ángulo de las manecillas; y v) calcule la hora indicando el número de la hora y los minutos. La entrada del programa es la imagen, la salida es la hora en el formato de dos números enteros. No es necesario determinar el número de segundos.

El algoritmo debe funcionar correctamente en las imágenes proporcionadas en la carpeta. No es necesario que funcione con otras imágenes o con otros relojes.

## Fecha de Entrega

Sábado 25 de marzo de 2023

## Informe (20%)

En el informe evalúa se calidad del informe, explicaciones, redacción, ortografía. El informe debe ser un PDF de una sola página (una cara en Times New Roman, Espacio Simple, Tamaño Carta, Tamaño de Letra 10,11 o 12), con márgenes razonables. El informe debe estar bien escrito en lenguaje formal, no coloquial ni anecdótico, sin faltas de ortografía y sin problemas de redacción. El informe debe contener: 1) Motivación: explicar la relevancia de la tarea. 2) Solución propuesta: explicar cada uno de los pasos y hacer referencia al código. 3) Experimentos realizados: explicar los experimentos, datos y los resultados obtenidos. 5) Conclusiones: mencionar las conclusiones a las que se llegó. 

## Solución Propuesta (50%)

A partir del enunciado, se debe implementar una solución en Python. El código debe ser debidamente comentado y explicado, por favor sea lo más claro posible para entender su solución, para hacer más fácil la corrección y para obtener mejor nota. Se evalúa la calidad del método, si el diseño es robusto y rápido para el problema dado, si los experimentos y los datos empleados son adecuados, si el código es entendible, limpio, ordenado y bien comentado.

## Restricciones

Las únicas librerías que se pueden usar son las siguientes 3:

* numpy

* cv2 (exclusivamente para usar la función imread que lee archivos jpg) y

* matplotlib para desplegar imagenes y otras gráficas.

## ATENCIÓN: LA IMPLEMENTACIÓN DEL ALGORITMO DEBE SER 100% PROPIA, NO SE PERMITE REUTILIZAR CÓDIGO HECHO POR OTRAS PERSONAS.

## Resultados Obtenidos (30%)

La nota en este ítem es 30% x C, donde C es A + B, con A un numero entre 0 y 1 que indica la mejor precisión encontrada en el curso y B constante calculada de tal forma que el mejor resultado en el curso obtenga C=1. A se define como (A1+A2+...+A5+A6)/6, donde Ai, la precisión en la imagen i, se calcula como (max(0,(10-Mi)/10)+max(0,(3-Hi)/3)/2 con Mi,Hi es el error en minutos en y horas respectiva en la estimación de la Hora.

## Indicaciones para enviar el trabajo

El trabajo debe enviarse al correo del profesor (joseiglesias@unicesar.edu.co)
