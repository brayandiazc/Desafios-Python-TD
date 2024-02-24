# Desafío evaluado - Estructuras de datos y funciones I

En este desafio se evaluarán las habilidades adquiridas en el modulo 3 unidad 3, estructuras de datos y funciones. Se evaluará la capacidad de manipulación de estructuras de datos, operaciones matemáticas, uso de librerias, arrays, diccionarios, manipulación de archivos y manipulación de datos.

## Ejercicios a desarrollar

1. **Conversión de monedas**
   - Tienes una cantidad de dinero en pesos chilenos, y necesitas saber cuánto es en otras monedas.
2. **Word_count**
   - Contar palabras y caracteres de un texto.
3. **Recordatorios**
   - Tines una lista de recordatorios, necesitas agregar uno nuevo.

### Conversión de monedas

Recuerda guardar el archivo con el nombre `conversiones.py`

```python

# Importa la libreria solicitada para recibir argumentos.
import ...

# Variables a utilizar OPCION A.
tasas = {
'...': ...,
'clp_parg': ...,
'...': float(sys.argv[3])
}

... = ...(sys.argv[4])

# Variables a utilizar OPCION B.
... = ...
clp_parg = ...
... = float(sys.argv[3])

... = ...(sys.argv[4])

# Operación de conversión, recuerda que la fórmula es...
...

# Mostar el resultado de la conversión.
print(f"Los {dinero} pesos equivalen a:")
print(f"...")
...
...
```

### Desafio Evaluado - Estructuras de datos y funciones - Word_count

Recuerda guardar el archivo con el nombre `word_count.py`

```python
# Importa la libreria solicitada para recibir argumentos.
... sys

# Leer el archivo, recuerda pasarlo como argumento, viene del material del desafio.
with open("texto.txt", "r") as file:
    texto=file.read()

# Contar caracteres.
... = len(...(texto))

# Contar palabras, recuerda que las palabras están separadas por espacios.
# Puedes usar el método split() para separar las palabras.
... = len(...)

# Output
print(f'El número de caracteres distintos es: {n_caracteres}')
print(f'El número de palabras distintas es: {n_palabras}')
```

### Desafio Evaluado - Estructuras de datos y funciones - Recordatorios

Recuerda guardar el archivo con el nombre `recordatorios.py`

```python
# Viene del material de apoyo.
recordatorios = [
	  ['2021-01-01', "11:00", "Levantarse y ejercitar"],
	  ['2021-05-01', "15:00", "No trabajar"],
	  ['2021-07-15', "13:00", "No hacer nada es feriado"],
	  ['2021-09-18', "16:00", "Ramadas"],
	  ['2021-12-25', "00:00", "Navidad"]
]

# Requerimiento 3.1.
recordatorios.insert(...,['2021-01-02', "06:00", "Empezar el año"])

# Requerimiento 3.2.
recordatorios[...][0] = "2021-07-16"

# Requerimiento 3.3.
recordatorios....(2)

# Requerimiento 3.4.
recordatorios...(...,['...', "...", "..."])
recordatorios.append(["..."])

# Mostrar los recordatorios.
...(recordatorios)
```
