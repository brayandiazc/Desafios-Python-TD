# Importa la clase Te desde el módulo te
from te import Te

# Pide al usuario que ingrese el sabor deseado de té
sabor = ...(input("¿Qué sabor de té desea? (Ingrese número de la opción)"
"\n1. Té negro \n2. Té verde \n3. Té de hierbas\n"))

# Pide al usuario que ingrese la cantidad de gramos deseada
... = ...(...("¿Qué formato desea?. Tenemos disponible"
" 300 y 500 gramos. Ingrese la cantidad de gramos deseada\n"))

# Llama a métodos estáticos de la clase Te para obtener el tiempo y la recomendación de preparación, y el precio
...

# Convierte el número del sabor a su texto correspondiente
...

# Imprime la información del pedido
print("Se ingresó su pedido de {}, en formato de {} gramos," 
"el cual tiene un valor de ${}. Este té tiene un tiempo "
"de preparación de {} minutos, y se recomienda su uso {}.".format(
    sabor_texto, formato, precio, tiempo, recomendacion
))
