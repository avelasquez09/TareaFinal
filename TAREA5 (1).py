import random
 
def dibujar(tablero):
  
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')
 
def cualLetra():

    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('Quiere jugar siendo X o O?')
        letra= input().upper()
 
 
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def quienJuegaPrimero():

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'pleyer '
 
def jugarOtra():
  
    print('Quiere Jugar de nuevo? (si o no)')
    return input().lower().startswith('si')
 
def hacerMovida(tablero, letra, movimiento):
    tablero[movimiento] = letra
 
def esGanador(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le))

def hacerCopia(tablero):

    tableroa = []
 
    for i in tablero:
        tableroa.append(i)
 
    return tableroa
 
def estaLibre(tablero, movimiento):

    return tablero[movimiento] == ' '
 
def movidaJugador(tablero):
  
    movimiento= ' '
    while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not estaLibre(tablero, int(movimiento)):
        print('Cual es su siguiente movimiento? (1-9)')
        movimiento = input()
    return int(movimiento)
 
def jugadaAleatoria(tablero, mlista):

    movidasPosibles = []
    for i in mlista:
        if estaLibre(tablero, i):
           mlista.append(i)
 
    if len(mlista) != 0:
        return random.choice(movidasPosibles)
    else:
        return None
 
def movidaPc(tablero, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 

    for i in range(1, 10):
        copia = hacerCopia(tablero)
        if estaLibre(copia, i):
            hacerMovida(copia, computerLetter, i)
            if esGanador(copia, computerLetter):
                return i
 

    for i in range(1, 10):
        copy = hacerCopia(tablero)
        if estaLibre(copia, i):
            hacerMovida(copia, playerLetter, i)
            if esGanador(copia, playerLetter):
                return i
 
  
    movimiento = jugadaAleatoria(tablero, [1, 3, 7, 9])
    if movimiento != None:
        return movimiento
 
  
    if isSpaceFree(tablero, 5):
        return 5
 

    return jugadaAleatoria(tablero, [2, 4, 6, 8])
 
def estaLleno(tablero):

    for i in range(1, 10):
        if estaLibre(tablero, i):
            return False
    return True
 
 
print('****TRIQUI*****!')
 
while True:
 
    elTablero = [' '] * 10
    playerLetter, computerLetter = cualLetra()
    turn = quienJuegaPrimero()
    print('El ' + turn + ' jugara de primero.')
    gameIsPlaying = True
 
    while gameIsPlaying:
         
        if turn == 'player':
           
            dibujar(elTablero)
            movimiento = movidaJugador(elTablero)
            hacerMovida(elTablero, playerLetter, movimiento)
 
            if esGanador(elTablero, playerLetter):
                dibujar(elTablero)
                print('Ganaste 1 vez')
                gameIsPlaying = False

                
            else:
                if estaLleno(elTablero):
                    dibujar(elTablero)
                    print('Empate')
                    break
                else:
                    turn = 'computer'
 


        else:
                 
            movimiento = movidaPc(elTablero, computerLetter)
            hacerMovida(elTablero, computerLetter, movimiento)
 
            if esGanador(elTablero, computerLetter):
                dibujar(elTablero)
                print('Perdiste.')
                gameIsPlaying = False
            else:
                if estaLleno(elTablero):
                   dibujar(elTablero)
                   print('Empate!')
                   break
                else:
                    turn = 'player'
 
    if not jugarOtra():
        print('GAME OVER')
