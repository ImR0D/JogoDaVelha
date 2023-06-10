import os

DIFFICULTY_MODE = ["PVP", "PVM_EASY", "PVM_MEDIUM"]
PLAYERS_NAME = ["JOGADOR 1", "JOGADOR 2", "MAQUINA"]
PLAYERS_TAG = {"JOGADOR 1": "X", "JOGADOR 2" : "O", "MAQUINA": "O"}

filledValues = []
session_players = []
current_player = PLAYERS_NAME[0]
winner = "None"
mode = DIFFICULTY_MODE[0]

os.system("title JOGO DA VELHA")

stage = [
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
["═", "═", "═", "╬", "═", "═", "═", "╬", "═", "═", "═"],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
["═", "═", "═", "╬", "═", "═", "═", "╬", "═", "═", "═"],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
[" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "]
]

# POSIÇÕES DO TABULEIRO DO JOGO DA VELHA
# PARA USAR -> POSSIBLES_POSITION[pos]
#
# Ex.: POSSIBLES_POSITION["TOP_LEFT"]
#
POSSIBLES_POSITION = {
    "TOP_LEFT": stage[1][1],
    "TOP_MIDDLE": stage[1][5],
    "TOP_RIGHT": stage[1][9],
    "CENTER_LEFT": stage[5][1],
    "CENTER_MIDDLE": stage[5][5],
    "CENTER_RIGHT": stage[5][9],
    "BOTTOM_LEFT": stage[9][1],
    "BOTTOM_MIDDLE": stage[9][5],
    "BOTTOM_RIGHT": stage[9][9]
}



"""
WIN_CONDITION = {
    1: {"TOP_1": stage[1][1], "TOP_2": stage[1][5], "TOP_3": stage[1][9]},              # TOP               HORIZONTAL
    2: {"MIDDLE_1": stage[5][1], "MIDDLE_2": stage[5][5], "MIDDLE_3": stage[5][9]},     # MIDDLE            HORIZONTAL
    3: {"BOTTOM_1": stage[9][1], "BOTTOM_2": stage[9][5], "BOTTOM_3": stage[9][9]},     # BOTTOM            HORIZONTAL
    4: {"LEFT_1": stage[1][1], "LEFT_2": stage[5][1], "LEFT_3": stage[9][1]},           # LEFT              VERTICAL
    5: {"CENTER_1": stage[1][5], "CENTER_2": stage[5][5], "CENTER_3": stage[9][5]},     # CENTER            VERTICAL
    6: {"RIGHT_1": stage[1][9], "RIGHT_2": stage[5][9], "RIGHT_3": stage[9][9]},        # RIGHT             VERTICAL
    7: {"LTRUPD_1": stage[1][1], "LTRUPD_2": stage[5][5], "LTRUPD_3": stage[9][9]},     # LEFT-TO-RIGHT     DIAGONAL UP-DOWN
    8: {"LTRDUP_1": stage[9][1], "LTRDUP_2": stage[5][5], "LTRDUP_3": stage[1][9]},     # LEFT-TO-RIGHT     DIAGONAL DOWN-UP
}
"""


def reset():
    stage[1][1] = " "
    stage[1][5] = " "
    stage[1][9] = " "
    stage[5][1] = " "
    stage[5][5] = " "
    stage[5][9] = " "
    stage[9][1] = " "
    stage[9][5] = " "
    stage[9][9] = " "
    filledValues.clear()
    session_players.clear()
    current_player = PLAYERS_NAME[0]
    WIN_CONDITION.clear()
    winner = "None"



# Posiciona a tag do jogador no tabuleiro e verifica se a posição está ou não preenchida
#
# setPosition("TOP_LEFT", PLAYERS_NAME[0])
def setPosition(pos, player):
    isValidPosition = False
    isValidValue = False

    for x in POSSIBLES_POSITION:
        if (pos == x):
            isValidPosition = True
    for y in PLAYERS_TAG:
        if (player == y):
            isValidValue = True

    if (isValidPosition and isValidValue):
        if pos == "TOP_LEFT" and stage[1][1] == " ":
            stage[1][1] = PLAYERS_TAG[player]
            filledValues.append(stage[1][1])
        elif pos == "TOP_MIDDLE" and stage[1][5] == " ":
            stage[1][5] = PLAYERS_TAG[player]
            filledValues.append(stage[1][5])
        elif pos == "TOP_RIGHT" and stage[1][9] == " ": 
            stage[1][9] = PLAYERS_TAG[player]
            filledValues.append(stage[1][9])
        elif pos == "CENTER_LEFT" and stage[5][1] == " ": 
            stage[5][1] = PLAYERS_TAG[player]
            filledValues.append(stage[5][1])
        elif pos == "CENTER_MIDDLE" and stage[5][5] == " ": 
            stage[5][5] = PLAYERS_TAG[player]
            filledValues.append(stage[5][5])
        elif pos == "CENTER_RIGHT" and stage[5][9] == " ":
            stage[5][9] = PLAYERS_TAG[player]
            filledValues.append(stage[5][9])
        elif pos == "BOTTOM_LEFT" and stage[9][1] == " ": 
            stage[9][1] = PLAYERS_TAG[player]
            filledValues.append(stage[9][1])
        elif pos == "BOTTOM_MIDDLE" and stage[9][5] == " ": 
            stage[9][5] = PLAYERS_TAG[player]
            filledValues.append(stage[9][5])
        elif pos == "BOTTOM_RIGHT" and stage[9][9] == " ":
            stage[9][9] = PLAYERS_TAG[player]
            filledValues.append(stage[9][9])
        else:
            return False
    else:
        return False

    return True

def isFieldsFilled():
    return True if (len(filledValues) >= 9) else False


def keyValidation(key):
    validKeys = [7, 8, 9, 4, 5, 6, 1, 2, 3]
    for k in validKeys:
        if key == k:
            return True
    return False

def sendCommand(command, player):
    isValidPlayer = False
    isValidCommand = keyValidation(command)

    for x in PLAYERS_NAME:
        if (player == x):
            isValidPlayer = True
            break
        else:
            isValidPlayer = False
    for y in session_players:
        if (player == y):
            isValidPlayer = True
            break
        else:
            isValidPlayer = False

    if (isValidPlayer and isValidCommand):
        match command:
            case 1:
                return setPosition("BOTTOM_LEFT", player)
            case 2:
                return setPosition("BOTTOM_MIDDLE", player)
            case 3:
                return setPosition("BOTTOM_RIGHT", player)
            case 4:
                return setPosition("CENTER_LEFT", player)
            case 5:
                return setPosition("CENTER_MIDDLE", player)
            case 6:
                return setPosition("CENTER_RIGHT", player)
            case 7:
                return setPosition("TOP_LEFT", player)
            case 8:
                return setPosition("TOP_MIDDLE", player)
            case 9:
                return setPosition("TOP_RIGHT", player)
    else:
        print("Comando inválido, ou usuário não encontrado!")


# Limpa a tela do console (Apenas via terminal/console)
def clearConsole():
    os.system("cls") or None
    setConsoleSize()

# Define o tamanho do console (30 linhas e 85 colunas)
def setConsoleSize():
    os.system("mode con lines=30 cols=85");

# Comandos básicos de jogabilidade
def showCommands():
    print("Comandos: \n")
    print("\t7 - Topo-Esquerda    |   8 - Topo-Meio    |   9 - Topo-Direita")
    print("\t4 - Centro-Esquerda  |   5 - Centro-Meio  |   6 - Centro-Direita")
    print("\t1 - Baixo-Esquerda   |   2 - Baixo-Meio   |   3 - Baixo-Direita\n")


# Pergunta se o usuário deseja continuar jogando
def playAgain():
        keepPlaying = input("\n\n\t\t\t   Deseja jogar novamente!? \n\nPressione qualquer tecla para continuar ou 'Q' para sair do jogo: ")
        if (keepPlaying.lower() == 'q'):
            print("Até breve! Espero você novamente para outra partida.\n\n")
            exit()
        else:
            openMenuView()


# Menu Inicial do Jogo
def openMenuView():
    clearConsole()
    option = 0
    menu = """
    ┌───────────────────────────────────────────────────────────────────────────┐
    │                                                                           │
    │ ▄▄▄▄▄▄  ▄▄▄  ▄▄▄▄▄   ▄▄▄    ▄▄▄▄    ▄▄▄▄    ▄   ▄ ▄▄▄▄▄ ▄    ▄   ▄  ▄▄▄▄  │
    │     █  █   █ █      █   █   █  ▐█  █    █   █   █ █     █    █   █ █    █ │
    │     █  █   █ █  ▄▄▄ █   █   █    █ █▄▄▄▄█   █   █ █▀▀▀  █    █▀▀▀█ █▄▄▄▄█ │
    │ █   █  █   █ █    █ █   █   █   █  █    █    █ █  █     █    █   █ █    █ │
    │  ▀▀▀    ▀▀▀   ▀▀▀▀   ▀▀▀    ▀▀▀▀   ▀    ▀     ▀   ▀▀▀▀▀ ▀▀▀▀ ▀   ▀ ▀    ▀ │
    │                                                                           │
    │                                                                           │
    │                                                                           │
    ├───────────────────────────────────────────────────────────────────────────┤
    │                                                                           │
    │                                                                           │
    │                             1)  Iniciar Jogo                              │
    │                                                                           │
    │                             2)  Modo de Jogo                              │
    │                                                                           │
    │                             3)  Sair do Jogo                              │
    │                                                                           │
    │                                                                           │
    └───────────────────────────────────────────────────────────────────────────┘
    """
    print(menu)
    option = int(input("Selecione uma opção: "))
    if (option == 1):
        gameBoard()
    elif (option == 2):
        openGameModeMenu()
    elif (option == 3):
        leave = input("Você realmente deseja sair? (S/N): ")
        if (leave.lower() == "s"):
            quit()
        else:
            openMenuView()


# Menu de Modo de Jogo
def openGameModeMenu():
    clearConsole()
    menu = """
    ┌───────────────────────────────────────────────────────────────────────────┐
    │                                                                           │
    │        ▄▄▄▄▄   ▄▄▄▄  ▄▄   ▄▄ ▄▄▄▄▄      ▄▄   ▄▄  ▄▄▄  ▄▄▄▄   ▄▄▄▄▄        │
    │        █      █    █ █ █ █ █ █          █ █ █ █ █   █ █  ▐█  █            │
    │        █  ▄▄▄ █▄▄▄▄█ █  █  █ █▀▀▀       █  █  █ █   █ █    █ █▀▀▀         │
    │        █    █ █    █ █  ▀  █ █          █  ▀  █ █   █ █  ▐█  █            │
    │         ▀▀▀▀  ▀    ▀ ▀     ▀ ▀▀▀▀▀      ▀     ▀  ▀▀▀  ▀▀▀▀   ▀▀▀▀▀        │
    │                                                                           │
    │                                                                           │
    ├───────────────────────────────────────────────────────────────────────────┤
    │                                                                           │
    │                    1)  Jogador vs Jogador     -- Padrão                   │
    │                                                                           │
    │                    2)  Jogador vs IA (Easy)   -- Ainda não implementado!  │
    │                                                                           │
    │                    3)  Jogador vs IA (Medium) -- Ainda não implementado!  │
    │                                                                           │
    │                    4)  Voltar ao menu                                     │
    │                                                                           │
    └───────────────────────────────────────────────────────────────────────────┘
    """
    print(menu)
    option = int(input("Selecione uma opção: "))
    if (option == 1):
        mode = DIFFICULTY_MODE[0]
        gameBoard()
    if (option == 2):
        #mode = DIFFICULTY_MODE[1]
        print("Ainda não implementado!")
        gameBoard()
    if (option == 3):
        #mode = DIFFICULTY_MODE[2]
        print("Ainda não implementado!")
        gameBoard()
    elif (option == 4):
        openMenuView()

# Menu do jogador vencedor
def gameWinner(player):
    clearConsole()
    win = """
    ┌───────────────────────────────────────────────────────────────────────────┐
    │                                                                           │
    │     ▄▄▄▄▄   ▄▄▄▄  ▄▄   ▄▄ ▄▄▄▄▄      ▄     ▄ ▄ ▄▄▄  ▄▄▄  ▄▄▄▄▄ ▄▄▄▄       │
    │     █      █    █ █ █ █ █ █          █     █ ▄ █  █ █  █ █     █   █      │
    │     █  ▄▄▄ █▄▄▄▄█ █  █  █ █▀▀▀       █  █  █ █ █  █ █  █ █▀▀▀  █  █       │
    │     █    █ █    █ █  ▀  █ █          █ █ █ █ █ █  █ █  █ █     █▀▀▀█      │
    │      ▀▀▀▀  ▀    ▀ ▀     ▀ ▀▀▀▀▀      ▀▀   ▀▀ ▀ ▀  ▀ ▀  ▀ ▀▀▀▀▀ ▀    ▀     │
    │                                                                           │
    ├───────────────────────────────────────────────────────────────────────────┤
    │                                                                           │
    │                                {} \t                                │
    │                                                                           │
    └───────────────────────────────────────────────────────────────────────────┘
    """.format(player)
    print(win)


# Menu do jogo empatado
def drawGame():
    clearConsole()
    draw = """
    ┌───────────────────────────────────────────────────────────────────────────┐
    │                                                                           │
    │      ▄▄▄▄   ▄▄▄▄    ▄▄▄▄  ▄     ▄       ▄▄▄▄▄   ▄▄▄▄  ▄▄   ▄▄ ▄▄▄▄▄       │
    │      █  ▐█  █   █  █    █ █     █       █      █    █ █ █ █ █ █           │
    │      █    █ █  █   █▄▄▄▄█ █  █  █       █  ▄▄▄ █▄▄▄▄█ █  █  █ █▀▀▀        │
    │      █  ▐█  █▀▀▀█  █    █ █ █ █ █       █    █ █    █ █  ▀  █ █           │
    │      ▀▀▀▀   ▀    ▀ ▀    ▀ ▀▀   ▀▀        ▀▀▀▀  ▀    ▀ ▀     ▀ ▀▀▀▀▀       │
    │                                                                           │
    └───────────────────────────────────────────────────────────────────────────┘
    """
    print(draw)


# Gerador de Estágio
def createStage():
    s = "\n\n"
    for i in range(len(stage)):
        s += "\n\t\t\t\t"
        for j in range(len(stage[i])):
            s += stage[i][j]
    print(s)


def setNewSession():
    global current_player, session_players
    reset()
    current_player = PLAYERS_NAME[0]
    if (mode == DIFFICULTY_MODE[0]):
        session_players = [PLAYERS_NAME[0], PLAYERS_NAME[1]]
    elif (mode == DIFFICULTY_MODE[1] or mode == DIFFICULTY_MODE[2]):
        session_players = [PLAYERS_NAME[0], PLAYERS_NAME[2]]


def alterPlayer():
    global current_player
    if (current_player == PLAYERS_NAME[0]):
        current_player = PLAYERS_NAME[1]
    else:
        current_player = PLAYERS_NAME[0]


WIN_CONDITION = []
def hasWinner():
    global WIN_CONDITION
    WIN_CONDITION = [
        [stage[1][1], stage[1][5], stage[1][9]], # TOP           HORIZONTAL
        [stage[5][1], stage[5][5], stage[5][9]], # MIDDLE        HORIZONTAL
        [stage[9][1], stage[9][5], stage[9][9]], # BOTTOM        HORIZONTAL
        [stage[1][1], stage[5][1], stage[9][1]], # LEFT          VERTICAL
        [stage[1][5], stage[5][5], stage[9][5]], # CENTER        VERTICAL
        [stage[1][9], stage[5][9], stage[9][9]], # RIGHT         VERTICAL
        [stage[1][1], stage[5][5], stage[9][9]], # LEFT-TO-RIGHT DIAGONAL UP-DOWN
        [stage[9][1], stage[5][5], stage[1][9]], # LEFT-TO-RIGHT DIAGONAL DOWN-UP
    ]
    for x in range(len(WIN_CONDITION)):
        global winner
        line = ""
        for y in range(len(WIN_CONDITION[x])):
            line += WIN_CONDITION[x][y]
            if (y % 2 == 0):
                if (line == "XXX"):
                    winner = PLAYERS_NAME[0]
                    return True
                elif (line == "OOO" and session_players[1] == PLAYERS_NAME[1]):
                    winner = PLAYERS_NAME[1]
                    return True
                elif (line == "OOO" and session_players[1] == PLAYERS_NAME[2]):
                    winner = PLAYERS_NAME[2]
                    return True
    return False


def gameBoard():
    setNewSession()
    while True:
        global hasWinnerGame
        global fieldsFilled
        global winner
        clearConsole()
        showCommands()
        print("\nSessão atual: " + str(session_players[0]) + " | " + str(session_players[1]) + "\t\t\tModo de jogo: " + mode)
        print("\nJogador atual: " + current_player)
        createStage()
        hasWinnerGame = hasWinner()
        fieldsFilled = isFieldsFilled()
        if (not fieldsFilled and winner == "None"):
            command = int(input("\n\nComando: "))
            isSend = sendCommand(command, current_player)
            if (isSend):
                alterPlayer()
        elif winner == "None":
            drawGame()
            playAgain()
        elif (hasWinnerGame):
            input("Vencedor: " + str(winner))
            fieldsFilled = False
            gameWinner(winner)
            winner = "None"
            playAgain()
        else:
            return False


if __name__ == "__main__":
        openMenuView()