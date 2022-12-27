"""Auxiliar de entrada de dados do teclado para o board"""
from time import sleep
from window import Board, Colors


class Validation():
    """Validação de dados"""
    def __init__(self) -> None:
        self.__board = Board()

    def __validation(self, tela: list, jogada: int, player: int, **player_esc) -> list:
        """Verifica se o local está vazio ou preenchido"""
        def verification(inicio: int, fim: int, key: int) -> (list | None):
            for indice, contador in enumerate(range(inicio, fim+1)):
                if jogada == contador:
                    if tela[key][indice] != '':
                        print(Colors.red +'este lugar já está '
                              'ocupado, escolha outro'+ Colors.end, '\n')
                        sleep(1.5)
                        return self.player_move(tela, player, player1_esc=player_esc['player1_esc'],
                                                              player2_esc=player_esc['player2_esc'])
                    match player:
                        case 0:
                            return self.__board.insert(tela,{'key1': key,
                                                             'key2': indice,
                                                             'token':player_esc['player1_esc']})
                        case 1:
                            return self.__board.insert(tela,{'key1': key,
                                                             'key2': indice,
                                                             'token':player_esc['player2_esc']})
                                                             
        valor_1 = verification(7, 9, key=0)
        if isinstance(valor_1, list):
            return valor_1
        valor_2 = verification(4, 6, key=1)
        if isinstance(valor_2, list):
            return valor_2
        valor_3 = verification(1, 3, key=2)
        if isinstance(valor_3, list):
            return valor_3

    def dispenser_token(self) -> (tuple | None):
        """Separa os tokens para os players"""
        decisao: str = str(input('Jogador 1, Escolha entre X ou O: ')).strip().upper()
        match decisao:
            case 'X':
                return ('X', 'O')
            case 'O':
                return ('O', 'X')
            case _:
                self.__board.clear_terminal()
                self.__board.header()
                print(Colors.red +'\nEscolha apenas entre X ou O'+Colors.end)

    def winner(self, tela: list) -> (str | bool):
        """Verifica quem foi o ganhador"""
        for i in range(3):  # Linhas
            if tela[i][0] == tela[i][1] and \
               tela[i][1] == tela[i][2] and tela[i][0] != '':
                return tela[i][0]

        for j in range(3):  # Colunas
            if tela[0][j] == tela[1][j] and \
               tela[1][j] == tela[2][j] and tela[0][j] != '':
                return tela[0][j]

        if tela[0][0] != '' and tela[0][0] == tela[1][1] and \
           tela[1][1] == tela[2][2]:  # Diagonal principal
            return tela[0][0]

        if tela[0][2] != '' and tela[0][2] == tela[1][1] and \
           tela[1][1] == tela[2][0]:  # Diagonal secundaria
            return tela[0][2]

        for i in range(3):
            for j in range(3):
                if tela[i][j] == '':  # Verificando se não há impate
                    return False

        return 'empate'

    def player_move(self, tela: list, player: int, **player_esc) -> list:
        """Faz o movimento do player"""
        try:
            jogada: int = int(input(f'\nJogador {2 if player == 1 else 1}, Faça a sua Jogada: '))
            if 10 > jogada > 0:
                return self.__validation(tela, jogada, player,
                                         player1_esc=player_esc['player1_esc'],
                                         player2_esc=player_esc['player2_esc'])

            print(Colors.red +'\nEsse local não existe! Escolha outro'+ Colors.end)
            sleep(1.5)
            self.player_move(tela, player, player1_esc=player_esc['player1_esc'],
                                           player2_esc=player_esc['player2_esc'])
        except ValueError:
            print(Colors.red +'Apenas numeros inteiros entre 9 e 1'+ Colors.end, '\n')
            self.player_move(tela, player, player1_esc=player_esc['player1_esc'],
                                           player2_esc=player_esc['player2_esc'])
