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