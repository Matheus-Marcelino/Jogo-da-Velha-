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


def decides_winner() -> None:
    """Decide quem foi o ganhador"""
    if cont_empate < cont_player1 > cont_player2:
        write_match_winner(Colors.green +'PARABÉNS, O JOGADOR 1 VENCEU!'+ Colors.end, 27, 3)
    elif cont_empate < cont_player2 > cont_player1:
        write_match_winner(Colors.green +'PARABÉNS, O JOGADOR 2 VENCEU!'+ Colors.end, 27, 3)
    elif cont_player2 < cont_empate > cont_player1:
        write_match_winner(Colors.yellow +'OS DOIS PERDERAM, A VELHA VENCEU!!'+ Colors.end, 25, 3)
    elif cont_player1 == cont_player2 == cont_empate:
        write_match_winner(Colors.yellow +'TODOS EMPATARAM???? IMPOSSÍVEL!'+ Colors.end, 26, 3)
        jogador = randint(0, 1)
    else:
        write_match_winner(Colors.yellow +'UM EMPATE?? COMO CHEGAMOS ATÉ AQUI?'+ Colors.end, 24, 3)
        jogador = randint(0, 1)


board, validacao = Board(), Validation()
tela = board.tela
jogador = round_counter = cont_empate = cont_player1 = cont_player2 = 0

try:
except KeyboardInterrupt:
    print(Colors.green +'Saindo às pressas? compreendo! até dps ;)'+Colors.end)
    sleep(1.8)

