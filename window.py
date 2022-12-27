"""Auxiliar visual e criação do board"""
from os import system, name
from time import sleep
from colorama import init

class Colors:
    """Cores para os textos"""
    init()
    end = '\033[m'
    yellow = '\033[1;33m'
    red = '\033[1;91m'
    green = '\033[1;92m'
    pink = '\033[1;35m'
    blue = '\033[1;34m'
    white = '\033[1m'
    underline = '\033[4m'


class Board:
    """Metodos para axulixar o board"""
    def __init__(self) -> None:
        self.tela: list = [['', '', ''],
                           ['', '', ''],
                           ['', '', '']]

    def insert(self, tela: list, data: dict[int, str]) -> list:
        """Insere uma string no board"""
        tela[data['key1']][data['key2']] = data['token']
        return tela

    def points_table(self, player: int, round_c: int, cont_mpt: int, player1_c: int, player2_c: int) -> None:
        """Tabela para a aparição dos pontos"""
        def dynamic_change_position(key: int, key_2: int, key_3: int) -> int:
            """Muda dinâmicamente os valores de acordo com a condição"""
            return key if player == key_2 else key_3
