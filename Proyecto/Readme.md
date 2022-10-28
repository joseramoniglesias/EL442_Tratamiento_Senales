# Proyecto Final asignatura Tratamiento de Señales: Segmentación de Pulmones
## Enunciado

El objetivo de este proyecto es segmentar los pulmones que están presentes en una radiografia de la base de datos [Shenzhen](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4256233/). Para este proyecto se han seleccionado sólo 40 radiografías de la base de datos original. La segmentación consiste en encontrar la imagen binaria que contiene los pulmones.

 <img width="442" alt="Imagen1" src="https://user-images.githubusercontent.com/38440709/198708359-e1be3677-19a2-4390-ae9d-9733785fb6cf.png">

Para este proyecto se debe probar el método propuesto en las 40 imágenes con sus correspondientes segmentaciones ideales disponibles en esta [carpeta](https://github.com/joseramoniglesias/Tratamiento_Senales/blob/main/Proyecto/project.zip). Una visualización de algunas de las imágenes y sus segmentaciones ideales se muestran a continuación:
 
 ![Imagen2](https://user-images.githubusercontent.com/38440709/198708512-87d5f9c0-bad8-4146-b88d-f81907fb9a24.png)
 
El algoritmo diseñado debe entregar una imagen binaria, y a la vez debe compararse con la segmentación ideal entregando por imagen los valores:
•	TP (true positives): número de pixeles pertenecientes a los pulmones correctamente segmentados
•	TN (true negatives): número de pixeles pertenecientes al fondo (no-pulmón) correctamente segmentados
•	FP (false positives): número de pixeles pertenecientes al fondo (no-pulmón) segmentados como pulmón
•	FN (false negatives): número de pixeles pertenecientes a pulmones segmentados como no-pulmón
Asimismo, se debe calcular el TPR (tasa de true positives) y el FPR (tasa de false positives) definidos respectivamente como TP/(TP+FN) y FP/(FP+TN), que idealmente deben ser 100% y 0%.
AGREGAR METRICA DE DESEMPEÑO (F1 Score):
F1 = 2xTP / (2xTP + FP + FN)
Esta permitido usar librerías clásicas de procesamiento de imágenes, pero no de machine learning. Todo lo que se use deben saber explicarlo.
Modalidad de Trabajo
Grupos de 4 personas
Idea del Proyecto
Se debe entregargit una página en formato PDF en la que se informe cómo piensan hacer el proyecto, esto corresponde al trabajo en clases E09 (ver fecha de entrega)( Tratamiento_Senales/Calendario.md at main · joseramoniglesias/Tratamiento_Senales (github.com)). Se debe indicar qué pasos van a seguir, qué métodos vistos en clase van a emplear, qué métodos no vistos en clases piensan estudiar, qué experimentos van a hacer y cualquier otro detalle de la solución que piensan implementar.
Presentación de Avance
En la presentación de avance (ver fecha de entrega) se debe mostrar el correcto funcionamiento de la segmentación en algunas imágenes (por ejemplo las más fáciles). La Presentación de Avances consiste de dos ítems (cada uno con un archivo que se debe enviar de manera grupal a más tardar a las 10:00am del día de la presentación (esta fecha no podrá ser flexible)):
1.	Un archivo PDF de al menos cuatro diapositivas en formato de presentación (como un archivo powerpoint convertido a PDF). El nombre del archivo debe ser AVANCE_GRUPO_xx.PDF donde xx es el número de grupo asignado. Las cuatro diapositivas que la presentación debe contener son: 1) Integrantes del grupo y número del grupo, 2) Descripción de qué se ha hecho (usar un diagrama como este ejemplo), y dar detalles de las estrategias usadas y de los experimentos realizados), 3) Resultados obtenidos, 4) Trabajo futuro. El archivo PDF se deberá enviar al profesor.
2.	Un video con una presentación de 5 minutos por grupo. EL video debe ser de 5 minutos exactos, cada 5 segundos de diferencia en el tiempo de duración del video será penalizado con 0.25 puntos en la nota del avance. La presentación debe hacerse de manera ordenada y planificada, sabiendo a priori qué se va a decir en cada diapositiva y quién lo va a decir (escoger a la persona del grupo que pueda hacer la mejor presentación oral). Por favor no improvisar en el momento de la presentación, es necesario tomarlo como si fuera un 'show' con un guion preestablecido. Ensayen con alguien y pregunten si esa persona ha entendido lo que han dicho. La idea de la presentación es que cada grupo pueda aprender de los otros grupos al compartir experiencias de éxito y de fracaso también. Para la presentación, deben estar presentes todos los miembros del grupo. El archivo MP4 del video se deberá enviar al profesor.
Presentación Final
La presentación final del proyecto consiste en una reunión de todos los integrantes del grupo con el profesor del curso en el laboratorio 101. La reunión dura 45 minutos y se hará entre 6am y 12m en un horario definido por el profesor. La puntualidad en la presentación será considerada en la nota. Ver planificación
La reunión conmigo de 45 minutos consta de una presentación tipo powerpoint, una demo y preguntas de la materia del curso.
La presentación tipo powerpoint debe incluir:
1.	Introducción (relevancia de este tema, en que consiste el proyecto, etc.),
2.	Revisión del estado del arte,
3.	Método propuesto en detalle (con un diagrama de bloques claro con todos los pasos y resultados intermedios como el de este ejemplo),
4.	Resultados obtenidos,
se debe calcular el TPR (tasa de true positives) y el FPR (tasa de false positives) definidos respectivamente como TP/(TP+FN) y FP/(FP+TN), que idealmente deben ser 100% y 0%.
SE DEBE AGREGAR METRICA DE DESEMPEÑO (F1 Score):
F1 = 2xTP / (2xTP + FP + FN)
5.	Conclusiones (que funciona bien, que funciona mal, que se puede mejorar, dificultades, trabajo futuro, que se aprendió, etc.) y
6.	Demo: La demo consiste en que ustedes presenten el software funcionando de la mejor manera posible (sin improvisaciones), deben planear muy bien que van a mostrar con buenos experimentos. Adicionalmente, deben realizar la segmentación en 5 imágenes nuevas de lunares (muy similares a la de esta base de datos de 40) que el profesor proporcionara en el momento de la demo. Para la evaluación de estas 5 imágenes se cuenta también con la segmentación ideal, que será usada para que calculen el TPR, FPR y F1.
En la presentación habrá preguntas orientadas tanto al proyecto como a cuanto entienden de la materia del curso (examen oral). Esto me servirá para poner notas individuales a cada integrante del grupo.
Nota
La nota del proyecto se calcula de la siguiente manera: 50% presentación, %25 resultados, 25% examen oral. En la nota se premia el esfuerzo más que los resultados, tendrá una mejor nota una persona que pruebe e invente métodos con resultados no tan buenos, que una persona que pruebe/encuentre una sola función con resultados buenos.

