# Importa la clase Pizza del módulo pizza
from pizza import Pizza

# Imprime el tamaño y el precio predeterminado de todas las pizzas
print("Todas las pizzas tienen un tamaño {} y un valor de {}".format(
    Pizza.tamanio, Pizza.precio
))

# Verifica si un elemento está en la lista de ingredientes válidos para la pizza
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Crea una instancia de la clase Pizza y realiza un pedido
...

# Imprime los detalles de la pizza pedida, incluyendo vegetales, proteína, tipo de masa y si es válida
...

# Verifica si la clase Pizza es válida como pizza
...