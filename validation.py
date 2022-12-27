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