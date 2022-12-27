"""Arquivo principal para rodar o jogo da velha"""
from time import sleep
from random import randint
from validation import Validation
from window import Board, Colors


def write_winner_round(text: str, space: int, break_spc: int, delay: int) -> None:
    """Escreve de forma formatada o vencedor"""
    board.clear_terminal()
    board.header()
    print(' ' * space, text, '\n'*break_spc)
    board.show(tela)
    board.clear_board(tela)
    sleep(delay)
    board.clear_terminal()


def write_match_winner(text: str, space: int, delay: int) -> None:
    """Escreve quem foi o ganhador geral"""
    board.clear_terminal()
    board.header()
    print(' ' * space, text)
    sleep(delay)


