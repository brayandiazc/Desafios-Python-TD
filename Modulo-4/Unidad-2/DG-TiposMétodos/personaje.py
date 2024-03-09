class Personaje():

    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} \
        NIVEL: {self.nivel} \
        EXP: {self.experiencia}"

    @estado.setter
    def estado(self, exp):
        tmp_exp = self.experiencia + exp

        while tmp_exp >= 100:
            self.nivel += 1
            tmp_exp -= 100

        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= 1
            else:
                tmp_exp = 0

        self.experiencia = tmp_exp

    def __lt__(self, other):
        return self.nivel < other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel

    def __eq__(self, other):
        return self.nivel == other.nivel

    def get_probabilidad_ganar(self, other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(input(
            f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
            "de probabilidades de ganarle al Orco.\n"
            "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
            "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
            "\n¿Qué deseas hacer?\n"
            "1. Atacar\n"
            "2. Huir\n"
        ))
