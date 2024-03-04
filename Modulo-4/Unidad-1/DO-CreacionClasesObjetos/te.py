class Te:
    """Clase que representa diferentes tipos de té y proporciona métodos para obtener información sobre ellos."""

    ...  # Duración predeterminada de la conservación del té en días

    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor):
        """Devuelve el tiempo de preparación y la recomendación para un tipo de té dado.

        Args:
            sabor (int): El tipo de té deseado. 1 para té negro, 2 para té verde, 3 para té de hierbas.

        Returns:
            tuple: Un par de valores que representan el tiempo de preparación en minutos y la recomendación para consumirlo.
        """
       ...

    @staticmethod
    def retorna_precio(formato):
        """Devuelve el precio del té según el formato de gramos.

        Args:
            formato (int): La cantidad de gramos de té deseada, puede ser 300 o 500.

        Returns:
            int: El precio correspondiente al formato especificado.
        """
        ...
