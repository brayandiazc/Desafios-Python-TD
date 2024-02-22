# Viene del material de apoyo
recordatorios = [
	['2021-01-01', "11:00", "Levantarse y ejercitar"],
	['2021-05-01', "15:00", "No trabajar"],
	['2021-07-15', "13:00", "No hacer nada es feriado"],
	['2021-09-18', "16:00", "Ramadas"],
	['2021-12-25', "00:00", "Navidad"]
]

# Requerimiento 3.1
recordatorios.insert(...,['2021-01-02', "06:00", "Empezar el año"])

# Requerimiento 3.2
recordatorios[...][0] = "2021-07-16"

# Requerimiento 3.3
recordatorios....(2)

# Requerimiento 3.4
recordatorios...(...,['...', "...", "..."])
recordatorios.append(["..."])

# Mostrar los recordatorios
...(recordatorios)