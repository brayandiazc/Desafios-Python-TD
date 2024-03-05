# Importa las listas de ingredientes desde el módulo ingredientes
...

# Define la clase Pizza
class Pizza:
    # Atributo tamaño predeterminado
    ...

    # Atributo precio predeterminado
    precio = 10000

    # Método estático para validar si un elemento está en una lista de posibles elementos
    @staticmethod
    def validar_elemento(solicitado, posibles):
        # Se convierte el elemento solicitado a minúsculas para una comparación insensible a mayúsculas
        return solicitado.lower() in posibles

    # Método para tomar un pedido de pizza
    def pedir(self):
        # Se solicita al usuario ingresar la proteína deseada
        ...

        # Se inicializa la lista de vegetales de la pizza
        self.vegetales = []

        # Se solicita al usuario ingresar los vegetales deseados
        # Se almacena el primer vegetal ingresado
        ...

        # Se solicita al usuario ingresar el segundo vegetal deseado
        # Se almacena el segundo vegetal ingresado
        ...

        # Se solicita al usuario ingresar el tipo de masa deseada
        ...

        # Se verifica si la pizza es válida, es decir, si los ingredientes ingresados son válidos
        ...
