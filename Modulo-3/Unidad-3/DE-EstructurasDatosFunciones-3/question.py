import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
'intermedias': [1,2,3],
'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    # Paso 5: Llamar al pool de preguntas de dificultad.
    preguntas = p.pool_preguntas[...]
    # Paso 6: Se debe escoger alguna de las opciones disponibles.

    global ...
    # escoger una pregunta
    n_elegido = ...choice(...[...])
    # eliminarla del ambiente global para no escogerla de nuevo
    ...[dificultad]...(n_elegido)
    # Paso 7: Desacoplar la pregunta en enunciado según la opción escogida y su respectivas alternativas mezcladas con la función shuffle_alt().
    pregunta = ...[f'pregunta_{...}']
    alternativas = ...(...)
    return pregunta['enunciado'], alternativas

  if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden,
    # pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')