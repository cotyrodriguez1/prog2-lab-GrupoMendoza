***Informe del Proyecto***
Este proyecto es una aplicación desarrollada en Django que permite gestionar ciudades y rutas entre ellas. La aplicación incluye funcionalidades como la creación de ciudades, la definición de rutas con distancias específicas y la búsqueda de la ruta más corta entre dos ciudades utilizando el algoritmo de Dijkstra. Este sistema está diseñado como una herramienta de planificación y análisis para usuarios interesados en explorar rutas óptimas entre diversas localidades.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Descripción del Trabajo Realizado***
Gestión de Ciudades y Rutas:

Se implementó un modelo para manejar las ciudades, con atributos como nombre, descripción, atracciones turísticas, clima promedio, y la mejor época para visitar.
También se creó un modelo para las rutas entre ciudades, que permite establecer distancias y relaciones entre ellas.

Algoritmo de Dijkstra:

Se desarrolló una función que implementa el algoritmo de Dijkstra para calcular la ruta más corta entre dos ciudades. Esto incluye el uso de estructuras eficientes como un heap para mantener el rendimiento del algoritmo.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Análisis de Complejidad Algorítmica de Dijkstra***

El algoritmo de Dijkstra tiene una complejidad de O(V + E log V), donde:

V es el número de vértices (ciudades en este caso).
E es el número de aristas (rutas entre ciudades).

Esta implementación utiliza un heap como cola de prioridad, lo que mejora la eficiencia en la extracción del nodo de menor distancia y la actualización de distancias para los vecinos. Aunque es eficiente para grafos densos, podría optimizarse para grafos más grandes o dispersos.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Estado Actual del Proyecto***
Funcionamiento:

Creación y gestión de ciudades y rutas.
Cálculo de la ruta más corta utilizando Dijkstra.

Limitaciones y áreas de mejora:

Con nuestro grupo quisimos agregar los puntos extras para que la interfaz sea mas agradable para los usuarios.
Por motivos personales de las intregrantes , no se pudo implementar. Disculpe profe la demora de la entrega , muchas gracias.
( Lo esencial esta :) )


