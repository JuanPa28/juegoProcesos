import random

# Definir preguntas y respuestas
preguntas = {
    '1) ¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra? / a) 12 horas b) 8 minutos c) 8 segundos': 'b',

    '2) ¿Cuál es la capital de España? / a) París b) Madrid c) Roma': 'b',

    '3) ¿Quién pintó La Mona Lisa? / a) Vincent Van Gogh b) Leonardo da Vinci c) Pablo Picasso': 'b',

    '4) ¿Cuál es el río más largo del mundo? / a) Nilo b) Amazonas c) Yangtze': 'a',

    '5) ¿Quién escribió "La Odisea"? / a) Homero b) Virgilio c) Dante Alighieri': 'a',

    '6) ¿Cuál es la moneda oficial de Japón? / a) Dólar japonés b) Yen japonés c) Euro': 'b',

    '7) ¿Quién es el autor de la famosa obra "Don Quijote de la Mancha"? / a) Miguel de Cervantes b) Gabriel García '
    'Márquez c) William Shakespeare': 'a',

    '8) ¿En qué país se encuentra la Torre Eiffel? / a) Alemania b) Francia c) Italia': 'b',

    '9) ¿Quién fue el primer hombre en pisar la Luna? / a) Neil Armstrong b) Yuri Gagarin c) Buzz Aldrin': 'a',

    '10) ¿Quién es el máximo goleador del DIM? / a) German Cano b) Falcao c) Neymar Jr.': 'a',

    '11) ¿En qué continente se encuentra el país de Kenia? / a) África b) Asia c) América': 'a',

    '12) ¿Quién escribió "El Principito"? / a) Antoine de Saint-Exupéry b) Victor Hugo c) Franz Kafka': 'a',

    '13) ¿En qué país se encuentra la ciudad de Petra, una de las nuevas siete maravillas del mundo? / a) Egipto b) '
    'Jordania c) Grecia': 'b',

    '14) ¿Quién es el autor de la famosa obra "El Quijote"? / a) Miguel de Cervantes b) Gabriel García Márquez c) '
    'William Shakespeare': 'a',

    '15) ¿Cuál es la capital de Australia? / a) Sídney b) Canberra c) Melbourne': 'b',

    '16) ¿Quién fue el primer presidente de los Estados Unidos? / a) George Washington b) Abraham Lincoln c) Thomas '
    'Jefferson': 'a',

    '17) ¿En que año fue James Rodriguez goleador del mundial? / a) 2022 b) 2014 c) 2010,': 'b',

    '18) ¿En que años fue campeón el Atletico Nacional de libertadores? / a) 1989 y 2016 b) No tiene libertadores c) '
    '1914 y 1939  ': 'a',

    '19) ¿Qué es la Sinergia? / a) Es la propiedad por la cual la capacidad de actuación de un sistema es superior a '
    'la de sus componentes sumados individualmente. b) Es la cantidad de variedad de un sistema, es decir, '
    'a la cantidad de desorden o incertidumbre que prevalece en una situación de elección con varias alternativas. c) '
    'Ningunas de las anteriores': 'a',

    '20) ¿Cuáles de las siguientes no es una definición de sistemas? / a) Conjunto de partes o componentes '
    'coordinados y en interacción, que persiguen un objetivo común. b) Grupo de partes que interactúan bajo las '
    'influencias de fuerzas en alguna interacción definida. c) Conjunto ordenado de operaciones sistemáticas que '
    'permite hacer un cálculo y hallar la solución de un tipo de problemas. ': 'c'
}

# Inicializar variables del juego
posiciones = [0, 0]
jugador = 0
ganador = False

# Definir castigos

castigos = {
    'Puente': -3,
    'Resbalón': -2,
    'Calavera': -posiciones[jugador]
}


# Función para generar preguntas aleatorias
def generar_pregunta():
    pregunta = random.choice(list(preguntas.keys()))
    print('\nPregunta: ', pregunta)
    respuesta_correcta = preguntas[pregunta]
    respuesta_usuario = input('Respuesta: ')
    if respuesta_usuario == respuesta_correcta:
        print('¡Respuesta correcta! Avanzas', dado, 'casillas.')
        return True
    else:
        castigo = random.choice(list(castigos.keys()))
        print('¡Respuesta incorrecta! Te aplicamos el castigo:', castigo)
        posiciones[jugador] += castigos[castigo]
        if posiciones[jugador] < 0:
            posiciones[jugador] = 0
        return False


# Función para mostrar el tablero
def mostrar_tablero():
    print('---------------------')
    for i in range(4):
        row = '| '
        for j in range(5):
            if i * 5 + j + 1 == posiciones[0]:
                row += '1 '
            elif i * 5 + j + 1 == posiciones[1]:
                row += '2 '
            else:
                row += '  '
            row += '| '
        print(row)
        print('---------------------')


# Comenzar el juego
print('¡Bienvenidos a Alcance la Estrella por Andres y Pablo!\n')

while not ganador:
    # Turno del jugador
    print('Turno del jugador', jugador + 1)
    input('Presiona Enter para lanzar el dado...')
    dado = random.randint(1, 6)
    posiciones[jugador] += dado
    if posiciones[jugador] > 20:
        posiciones[jugador] = 20
    mostrar_tablero()
    if posiciones[jugador] == 20:
        print('¡El jugador', jugador + 1, 'ha ganado!')
        ganador = True
    else:
        acierto = generar_pregunta()
        if not acierto:
            print('El jugador', jugador + 1, 'se encuentra en la casilla', posiciones[jugador])
            jugador = (jugador + 1) % 2
            print('El jugador', jugador + 1, 'se encuentra en la casilla', posiciones[jugador])

print('\n¡Gracias por jugar!')
