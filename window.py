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
