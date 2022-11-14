from pyswip import Prolog
prolog = Prolog()
prolog.consult("2048.pl")
board = list(prolog.query("generate(Board)."))[0]["Board"]
prolog.asserta(f'board({board})')


def generate_board():
    global board
    prolog.retractall('board(_)')
    board = list(prolog.query("generate(Board)."))[0]["Board"]
    prolog.asserta(f'board({board})')
    return board


def move_up():
    global board
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    board = list(prolog.query("once(moveUp(Board, NewBoard))."))[0]["NewBoard"]
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    check_quit = check_lose_or_win()
    if check_quit is None:
        update_desk()
        return True
    else:
        return check_quit


def move_left():
    global board
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    board = list(prolog.query("once(pyLeft(Board, NewBoard))."))[0]["NewBoard"]
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    check_quit = check_lose_or_win()
    if check_quit == "You win!" or check_quit == "You lose":
        return check_quit
    else:
        update_desk()
        return True


def move_right():
    global board
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    board = list(prolog.query("once(moveRight(Board, NewBoard))."))[0]["NewBoard"]
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    check_quit = check_lose_or_win()
    if check_quit == "You win!" or check_quit == "You lose":
        return check_quit
    else:
        update_desk()
        return True


def move_down():
    global board
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    board = list(prolog.query("once(moveDown(Board, NewBoard))."))[0]["NewBoard"]
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    check_quit = check_lose_or_win()
    if check_quit == "You win!" or check_quit == "You lose":
        return check_quit
    else:
        update_desk()
        return True


def update_desk():
    global board
    board = list(prolog.query("addNew2(Board, NewBoard)."))[0]["NewBoard"]
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    return board


def check_lose_or_win():
    global board
    prolog.retractall('board(_)')
    prolog.assertz(f'board({board})')
    answer = list(prolog.query("game(Board, GameCheck)."))
    if len(answer) > 0:
        return answer[0]["GameCheck"]
    else:
        return None