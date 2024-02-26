# Desafío evaluado - Estructuras de datos y funciones II

En este desafio se evaluarán las habilidades adquiridas en el modulo 3 unidad 3, estructuras de datos y funciones. Se evaluará la capacidad de manipulación de estructuras de datos, operaciones matemáticas, uso de librerias, arrays, diccionarios, manipulación de archivos y manipulación de datos.

## Ejercicios a desarrollar

Refactorizar el código del proyecto

### Requerimiento 1 `validator.py`

```python
def validate(opciones, eleccion):
   # Paso 1: Un ciclo while que no termine si es que la elección dada no es parte de las opciones.
   while eleccion not in opciones:
   # Paso 2:  solicitar mediante input una elección nueva que sí esté entre las opciones dadas
   eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
   return eleccion


if __name__ == '__main__':
   eleccion = input('Ingresa una Opción: ').lower()
   # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
   numeros = ['0','1']
   # Si se ingresan valores no válidos a eleccion debe seguir preguntando
   validate(numeros, eleccion)
```

### Requerimiento 2 `level.py`

```python
def choose_level(n_pregunta, p_level):
   # Paso 3: número de pregunta y las preguntas por nivel mediante un if/elif/else
   if n_pregunta <= ...:
      ... = 'basicas'
   elif ... <= 2*...:
      ... = 'intermedias'
   else:
      ... = 'avanzadas'

   return level

if __name__ == '__main__':
   # verificar resultados
   print(choose_level(2, 2)) # básicas
   print(choose_level(3, 2)) # intermedias
   print(choose_level(7, 2)) # avanzadas
   print(choose_level(4, 3)) # intermedias
```

### Requerimiento 3 `shuffle.py`

```python
import preguntas as p
import random

def shuffle_alt(pregunta):
   # Paso 4: Tomar de las preguntas sólo la clave correspondiente a alternativas y estas deben ser mezcladas.

   random.shuffle(...['...'])
   return pregunta['alternativas']

if __name__ == '__main__':
   # si se ejecuta el programa varias veces las alternativas
   # debieran aparecer en distinto orden
   print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))
   # a modo de ejemplo
   # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
```

### Requerimiento 4 `question.py`

```python

```
