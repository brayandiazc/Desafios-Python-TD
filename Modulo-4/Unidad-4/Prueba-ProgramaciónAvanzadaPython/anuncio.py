# Importa la clase ABC y la función abstractmethod del módulo abc
from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

# Definición de la clase Anuncio como clase abstracta
class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str,
            url_clic: str, sub_tipo: str) -> None:
        # Inicializa los atributos del anuncio
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    # Método de propiedad para acceder al ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    ...

    # Método de propiedad para acceder al alto
    ...

    # Método setter para el alto
    ...

    # Siguen los metodos
    ...

    # Método setter para el subtipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS
        or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS
        or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub tipo indicado no está permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos() -> None:  # Método estático para mostrar los formatos disponibles
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")

        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")

    @abstractmethod
    def comprimir_anuncios(self) -> None:  # Método abstracto para comprimir los anuncios
        pass

    @abstractmethod
    def redimensionar_anuncio(self) -> None:  # Método abstracto para redimensionar los anuncios
        pass

    # Sigue el codigo