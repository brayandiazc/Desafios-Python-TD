# Importando DimensionError desde el módulo error
from error import DimensionError

class Foto():
    # Dimensión máxima permitida para la foto
    MAX = 2500

    # Constructor que inicializa el ancho, el alto y la ruta de la foto
    ...

    # Método de propiedad para acceder al ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, ancho) -> None:
        # Comprueba si el ancho excede el límite máximo
        if ancho > Foto.MAX:
            raise DimensionError("Ancho no permitido.", ancho, Foto.MAX)
        # Comprueba si el ancho es menor que 1
        elif ancho < 1:
            raise DimensionError("Ancho debe ser mayor a 0.", ancho)
        else:
            # Establece el ancho
            self.__ancho = ancho

    # Método de propiedad para acceder al alto
    ...

    @alto.setter
    ...
