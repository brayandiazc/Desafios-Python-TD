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