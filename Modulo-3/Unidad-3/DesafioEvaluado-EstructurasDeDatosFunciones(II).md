# Desafío evaluado - Estructuras de datos y funciones II

En este desafio se evaluarán las habilidades adquiridas en el modulo 3 unidad 3, estructuras de datos y funciones. Se evaluará la capacidad de manipulación de estructuras de datos, operaciones matemáticas, uso de librerias, arrays, diccionarios, manipulación de archivos y manipulación de datos.

## Ejercicios a desarrollar

1. **Filtrado relevante**
   - Filtrar datos relevantes de un diccionario.
2. **Alertas telemáticas**
   - Calcular velocidad promedio y mostrar alertas.
3. **Apoyo matemático**
   - Programar operaciones avanzadas.

### Filtrado relevante

Recuerda guardar el archivo con el nombre `filtro.py`

```python
# Paso 1: Importar el módulo sys para usar argumentos de la línea de comandos
import sys

# Obtener el umbral desde los argumentos de la línea de comandos. Convertirlo a float para manejar números con decimales.
umbral = float(sys.argv[1])

# Definir el diccionario de productos con sus precios
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Paso 2: Definir la función para filtrar los productos
# Esta función debe recibir el diccionario de precios, el umbral y un valor por defecto que indica si filtrar por mayor o menor
...
    # Completar: Inicializar una lista vacía para guardar los nombres de los productos filtrados
    filtro = []

    if mayor_que:
        # Completar: Usar una comprensión de lista para filtrar productos cuyo precio sea mayor que el umbral
        # Deberías iterar sobre diccionario.items() y agregar el nombre del producto a la lista si cumple la condición
        pass  # Remover esta línea después de completar la tarea
    ...
        # Completar: Similar al bloque anterior, pero para productos con precio menor que el umbral
        pass  # Remover esta línea después de completar la tarea

    # Paso 4: Imprimir los resultados
    # Completar: Usar .join() para convertir la lista de nombres de productos en una cadena de texto formateada
    # Imprimir el mensaje adecuado según si el filtro es por mayor o menor que el umbral

# Paso 5: Controlar el flujo del script basado en los argumentos proporcionados
if len(sys.argv) == 2:
    # Llamar a la función filtrar solo con el umbral, usando el valor por defecto para 'mayor_que'
    filtrar(precios, umbral)
else:
    # Completar: Verificar si el segundo argumento es 'mayor' o 'menor' y llamar a la función filtrar con el valor adecuado para 'mayor_que'
    # En caso de recibir un valor no esperado para el segundo argumento, imprimir un mensaje de error.

```

### Alertas telemáticas

Recuerda guardar el archivo con el nombre `velocidad.py`

```python
# Paso 1: Definir la lista de velocidades
velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21
]

# Paso 2: Definir una función para calcular el promedio de las velocidades
# Esta función toma como parámetro una lista de números (velocidades) y devuelve su promedio.
...

# Paso 3: Definir una función para filtrar las velocidades superiores al promedio
# Esta función toma como parámetro la lista de velocidades y utiliza la función promedio para obtener el valor medio.
...
    # Primero, calculamos el promedio de las velocidades usando la función promedio definida anteriormente.
    ...
    # Luego, usamos una comprensión de lista para obtener las posiciones de las velocidades superiores al promedio.
    # La función enumerate() es útil aquí para obtener tanto el índice (posición) como el valor de cada elemento en la lista.
    return [i for i, v in enumerate(velocidad) if v > valor_promedio]

# Paso 4: Imprimir el resultado de la función filtrar
# Esto mostrará las posiciones de las correas transportadoras con velocidades superiores al promedio.
...
```

### Apoyo matemático

Recuerda guardar el archivo con el nombre `ong.py`

```python
# Paso 1: Definir la función para calcular la productoria de una lista de números
def productoria(lista):
    # Inicializar una variable para almacenar el resultado de la productoria
    resultado = 1
    # Iterar sobre cada elemento de la lista y multiplicarlo por el resultado acumulado
    for elemento in lista:
        resultado *= elemento
    # Retornar el resultado de la productoria
    ...

# Paso 2: Definir la función para calcular el factorial de un número
def factorial(n):
    # Inicializar una variable para almacenar el resultado del factorial
    resultado = 1
    # Iterar sobre un rango de 1 a n (inclusive) y multiplicar cada número por el resultado acumulado
    for numero in range(1, n + 1):
        ...
    # Retornar el resultado del factorial
    ...

# Paso 3: Definir una función que maneje los cálculos basada en los parámetros recibidos
def calcular(**parametros):
    # Iterar sobre cada par clave-valor de los parámetros
    for clave, valor in parametros.items():
        # Determinar si la clave indica un cálculo de factorial
        if 'fact' in clave:
            # Completar: Llamar a la función factorial y imprimir el resultado con un mensaje adecuado
            pass  # Remover esta línea después de completar la tarea
        # Determinar si la clave indica un cálculo de productoria
        elif 'prod' in clave:
            # Completar: Llamar a la función productoria y imprimir el resultado con un mensaje adecuado
            pass  # Remover esta línea después de completar la tarea

# Paso 4: Ejecutar la función calcular con ejemplos de factorial y productoria
# Completar: Llamar a la función calcular con diferentes combinaciones de argumentos para probar su funcionamiento
```
