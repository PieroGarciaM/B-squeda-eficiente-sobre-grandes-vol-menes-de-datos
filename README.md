📊 Comparación de Estructuras de Datos y Rendimiento
📌 Descripción del Proyecto

Este proyecto tiene como objetivo analizar el rendimiento de distintas estructuras de datos al trabajar con grandes volúmenes de información.

El programa:

Genera 10,000,000 de números aleatorios en el rango de -50,000,000 a 50,000,000.

Los almacena en un archivo de texto.

Carga los datos en memoria.

Construye distintas estructuras de datos.

Ejecuta búsquedas manuales.

Realiza 1,000 búsquedas automáticas por cada estructura.

Calcula el tiempo promedio de búsqueda.

Presenta una tabla comparativa de rendimiento.

🏗️ Estructuras de Datos Utilizadas
1️⃣ Lista (Búsqueda Lineal)

Recorre los elementos uno por uno.

No requiere ordenamiento.

Complejidad: O(n)

2️⃣ Lista Ordenada (Búsqueda Binaria)

Requiere ordenar previamente los datos.

Divide el espacio de búsqueda en mitades sucesivas.

Complejidad: O(log n)

3️⃣ Tabla Hash (Diccionario en Python)

Utiliza función hash para acceso directo.

No requiere ordenamiento.

Mayor consumo de memoria.

Complejidad promedio: O(1)

⚙️ Funcionamiento del Programa

Generación de datos masivos.

Carga en memoria.

Construcción de:

Lista original

Lista ordenada

Tabla hash

Ejecución de 1,000 búsquedas automáticas por estructura.

Cálculo del tiempo promedio.

Presentación de tabla comparativa.

📈 Resultados de Rendimiento
Estructura	Tiempo Promedio (s)	Memoria Aproximada	Complejidad
Lista (Lineal)	(resultado obtenido)	Baja	O(n)
Lista Ordenada	(resultado obtenido)	Media	O(log n)
Tabla Hash	(resultado obtenido)	Alta	O(1)

(Los valores reales dependen del hardware utilizado.)

🧠 Análisis

La búsqueda lineal mostró crecimiento proporcional al tamaño de los datos, confirmando su complejidad O(n).

La búsqueda binaria demostró alta eficiencia tras el ordenamiento inicial.

La tabla hash presentó tiempos prácticamente constantes, aunque con mayor uso de memoria.

Se concluye que:

Para pocas búsquedas, puede no valer la pena ordenar.

Para muchas búsquedas, la búsqueda binaria es altamente eficiente.

Cuando la memoria no es un problema y se requieren búsquedas masivas, la tabla hash es la mejor opción.

💻 Requisitos

Python 3.x

16GB RAM recomendados para ejecución con 10 millones de datos

▶️ Cómo Ejecutar
python main.py

El programa generará automáticamente el archivo de datos si no existe.

🎓 Conclusión Final

Este proyecto permitió comprobar empíricamente cómo diferentes estructuras de datos impactan el rendimiento en escenarios de gran escala.

Se demostró que la elección de la estructura adecuada depende del contexto, la cantidad de búsquedas y las restricciones de memoria.
