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