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

        print(' ' * 34,Colors.underline + Colors.yellow +f'Vez do jogador {dynamic_change_position(2, 1, 1) }'+ Colors.end, '\n')
        print(' ' * 34, Colors.blue +f' Rodada{Colors.end}{Colors.white}:{Colors.end} {Colors.blue}{round_c}/5{Colors.end}\n',
              ' ' * 34, Colors.yellow +f'Jogador {dynamic_change_position(2, 1, 1)}{Colors.end}{Colors.white}:{Colors.end} '
                                       f'{Colors.yellow}{dynamic_change_position(player2_c, 1, player1_c)}{Colors.end}\n',
              ' ' * 34, Colors.yellow +f'Jogador {dynamic_change_position(2, 0, 1)}{Colors.end}: '
                                       f'{Colors.yellow}{dynamic_change_position(player2_c, 0, player1_c)}{Colors.end}\n',
              ' ' * 34, Colors.blue +f'Velha{Colors.end}{Colors.white}:{Colors.end} {Colors.blue}{cont_mpt}{Colors.end}', '\n'*2)

    def clear_terminal(self) -> None:
        """Limpa o terminal"""
        system("cls") if name == "nt" else system("clear")

    def clear_board(self, tela: list) -> list:
        """Retira todas as strings do board"""
        for i in range(3):
            for j in range(3):
                tela[i][j] = ''
        return tela

    def header(self) -> None:
        """Mostra o cabeçalho"""
        print(' ' * 25, Colors.pink + '-=-' * 11 + Colors.end)
        print(' ' * 35, Colors.white + 'JOGO DA VELHA' + Colors.end)
        print(' ' * 25, Colors.pink + '-=-' * 11 + Colors.end, '\n' * 3)

    def tutorial(self) -> None:
        """Mostra um tutorial simples de como mexer no board"""
        print(' ' * 13,'Os números indicam o mesmo campo onde será colocado o '
                        f'{Colors.green}X{Colors.end} e o {Colors.green}O{Colors.end}\n')
        print(f'{7:>35}   |{8:^7}|{9:>3}')
        print(' ' * 28, '=-=' * 9)
        print(f'{4:>35}   |{5:^7}|{6:>3}')
        print(' ' * 28, '=-=' * 9)
        print(f'{1:>35}   |{2:^7}|{3:>3}')
        sleep(10)
        print('\n', ' ' * 36, Colors.yellow +'Bom Jogo!'+ Colors.end)
        sleep(1.5)

    def show(self, tela: list) -> None:
        """Mostra o board na tela"""
        print(f'{tela[0][0]:>35}   |{tela[0][1]:^7}|{tela[0][2]:>3}')
        print(' ' * 28, '=-=' * 9)
        print(f'{tela[1][0]:>35}   |{tela[1][1]:^7}|{tela[1][2]:>3}')
        print(' ' * 28, '=-=' * 9)
        print(f'{tela[2][0]:>35}   |{tela[2][1]:^7}|{tela[2][2]:>3}')
