% Доска выглядит как:
%   A1 A2 A3 A4
%   B1 B2 B3 B4
%   C1 C2 C3 C4
%   D1 D2 D3 D4
%  и используется как list:
%   [A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4]
play :-
	generate(Board),
	showBoard(Board),
	printHelp,
	game(Board).
boardScore(Board, Score) :-
    board(Board),
	squared(Board, Squared),
	sum_list(Squared, Score).
squared([], []).
squared([H1|T1], [H2|T2]) :-
	H2 is H1 * H1,
	squared(T1,T2).
game(Board, GameCheck) :-
    board(Board),
	max_list(Board, 2048),
	GameCheck = "You win!".
game(Board, GameCheck) :-
    board(Board),
	noMoreMoves(Board),
	GameCheck = "You lose".

% game(Board) :-
%    board(Board),
%	nl,write('Your move? '),
%	get_single_char(X),
%	move(Board, X, B),
%	(equal(Board, B) ->
%		(write('Cant move that way.'),nl,game(Board)) ;
%		(addNew(B,NewBoard),showBoard(NewBoard),game(NewBoard))).
noMoreMoves(Board) :-
    board(Board),
	once(moveLeft(Board, X)),
	equal(Board, X),
	once(moveRight(Board, Y)),
	equal(Board, Y),
	once(moveUp(Board, Z)),
	equal(Board,Z),
	once(moveDown(Board, W)),
	equal(Board,W).
equal([],[]).
equal([H1|T1],[H2|T2]) :-
	H1 == H2,
	equal(T1,T2).
move(Board, 119, NewBoard) :-
    board(Board),
	write('up'),nl,nl,
	once(moveUp(Board, NewBoard)).
move(Board, 107, NewBoard) :-
    board(Board),
	write('up'),nl,nl,
	once(moveUp(Board, NewBoard)).
move(Board, 115, NewBoard) :-
    board(Board),
	write('down'),nl,nl,
	once(moveDown(Board, NewBoard)).
move(Board, 106, NewBoard) :-
    board(Board),
	write('down'),nl,nl,
	once(moveDown(Board, NewBoard)).
move(Board, 97, NewBoard) :-
    board(Board),
	write('left'),nl,nl,
	once(moveLeft(Board, NewBoard)).
move(Board, 104, NewBoard) :-
    board(Board),
	write('left'),nl,nl,
	once(moveLeft(Board, NewBoard)).
move(Board, 100, NewBoard) :-
    board(Board),
	write('right'),nl,nl,
	once(moveRight(Board, NewBoard)).
move(Board, 108, NewBoard) :-
    board(Board),
	write('right'),nl,nl,
	once(moveRight(Board, NewBoard)).
move(_, 113, _) :-
    board(Board),
	write('quit'),nl,nl,
	write('Bye...'), nl,nl,
	abort.
move(Board, 98, _) :-
    board(Board),
	write('show board'),nl,
	showBoard(Board), game(Board).
move(Board, _, _) :-
    board(Board),
	nl,write('Illegal move! Press ? for help.'),nl,
	game(Board).
generate(Board):-
    addNew([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],B),
	addNew(B,Board).
rotateRight([A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4],[E1,E2,E3,E4,F1,F2,F3,F4,G1,G2,G3,G4,H1,H2,H3,H4]) :-
	E1 is D1,
	E2 is C1,
	E3 is B1,
	E4 is A1,
	F1 is D2,
	F2 is C2,
	F3 is B2,
	F4 is A2,
	G1 is D3,
	G2 is C3,
	G3 is B3,
	G4 is A3,
	H1 is D4,
	H2 is C4,
	H3 is B4,
	H4 is A4.
rotateLeft([A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4],[E1,E2,E3,E4,F1,F2,F3,F4,G1,G2,G3,G4,H1,H2,H3,H4]) :-
	E1 is A4,
	E2 is B4,
	E3 is C4,
	E4 is D4,
	F1 is A3,
	F2 is B3,
	F3 is C3,
	F4 is D3,
	G1 is A2,
	G2 is B2,
	G3 is C2,
	G4 is D2,
	H1 is A1,
	H2 is B1,
	H3 is C1,
	H4 is D1.
moveUp(Board, NewBoard):-
    board(Board),
	rotateLeft(Board, Temp1),
	moveLeft(Temp1, Temp2),
	rotateRight(Temp2, NewBoard).
moveDown(Board, NewBoard):-
    board(Board),
	rotateRight(Board, Temp1),
	moveLeft(Temp1, Temp2),
	rotateLeft(Temp2, NewBoard).
moveRight(Board, NewBoard):-
    board(Board),
	rotateLeft(Board, Temp1),
	rotateLeft(Temp1, Temp2),
	moveLeft(Temp2, Temp3),
	rotateRight(Temp3, Temp4),
	rotateRight(Temp4, NewBoard).
moveLeft([], []).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X3 \= 0,
	X1 == X2,
	X3 == X4,
	N1 is X1 + X2,
	N2 is X3 + X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X, N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X1 == X2,
	X2 == X3,
	N1 is X1 + X2,
	N2 is X3,
	N3 is X4,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X1 == X2,
	X3 \= 0,
	N1 is X1 + X2,
	N2 is X3,
	N3 is X4,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 \= 0,
	X1 \= X2,
	X2 \= X3,
	X3 == X4,
	N1 is X1,
	N2 is X2,
	N3 is X3 + X4,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 \= 0,
	X2 == X3,
	N1 is X1,
	N2 is X2 + X3,
	N3 is X4,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X2 == 0,
	X3 == 0,
	N1 is X4,
	N2 is 0,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X2 == 0,
	X3 == X4,
	N1 is X3 + X4,
	N2 is 0,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X2 == 0,
	N1 is X3,
	N2 is X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X3 == 0,
	X2 == X4,
	N1 is X2 + X4,
	N2 is 0,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X3 == 0,
	N1 is X2,
	N2 is X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X2 == X3,
	N1 is X2 + X3,
	N2 is X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X2 \= 0,
	X3 \= 0,
	X2 \= X3,
	X3 \= X4,
	N1 is X2,
	N2 is X3,
	N3 is X4,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 == 0,
	X2 \= 0,
	X3 == X4,
	N1 is X2,
	N2 is X3 + X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 == 0,
	X3 == X4,
	N1 is X1,
	N2 is X3 + X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 == 0,
	X1 == X3,
	N1 is X1 + X3,
	N2 is X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 == 0,
	X3 \= 0,
	N1 is X1,
	N2 is X3,
	N3 is X4,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 == 0,
	X3 == 0,
	X1 == X4,
	N1 is X1 + X4,
	N2 is 0,
	N3 is 0,
	N4 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 == 0,
	X3 == 0,
	N1 is X1,
	N2 is X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X1 == X2,
	X3 == 0,
	N1 is X1 + X2,
	N2 is X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 \= 0,
	X1 \= X2,
	X3 == 0,
	X2 == X4,
	N1 is X1,
	N2 is X2 + X4,
	N3 is 0,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 \= 0,
	X3 == 0,
	N1 is X1,
	N2 is X2,
	N3 is X4,
	N4 is 0,
	moveLeft(X,N).
moveLeft([X1,X2,X3,X4|X], [N1,N2,N3,N4|N]) :-
	X1 \= 0,
	X2 \= 0,
	X3 \= 0,
	N1 is X1,
	N2 is X2,
	N3 is X3,
	N4 is X4,
	moveLeft(X,N).
addNew2(Board, NewBoard) :-
    board(Board),
	countZeros(Board, Z),
	position(Z, P),
	twoOrFour(N),
	replaceZero(Board, P, N, NewBoard).
addNew(Board, NewBoard) :-
	countZeros(Board, Z),
	position(Z, P),
	twoOrFour(N),
	replaceZero(Board, P, N, NewBoard).
countZeros([], 0).
countZeros([H|T], N) :-
	H == 0,
	countZeros(T, W),
	N is W + 1.
countZeros([H|T], N) :-
	H \= 0,
	countZeros(T, N).
position(NumberOfZeros, P) :-
	P is random(NumberOfZeros).
twoOrFour(N) :-
	P is random(10),
	P < 9 -> N is 2 ; N is 4.
replaceZero([],_,_,[]).
replaceZero([H1|T1], P, N, [H2|T2]) :-
	H1 == 0,
	P == 0,
	H2 is N,
	replaceZero(T1, -1, N, T2).
replaceZero([H1|T1], P, N, [H2|T2]) :-
	H1 == 0,
	P > 0,
	Pn is P - 1,
	H2 is H1,
	replaceZero(T1, Pn, N, T2).
replaceZero([H1|T1], P, N, [H2|T2]) :-
	H1 == 0,
	P < 0,
	H2 is H1,
	replaceZero(T1, P, N, T2).
replaceZero([H1|T1], P, N, [H2|T2]) :-
	H1 \= 0,
	H2 is H1,
	replaceZero(T1, P, N, T2).
showBoard([]).
showBoard([H|T]) :-
	printNumber(H),
	showBoard1(T).
showBoard1([H|T]) :-
	printNumber(H),
	showBoard2(T).
showBoard2([H|T]) :-
	printNumber(H),
	showBoard3(T).
showBoard3([H|T]) :-
	printNumber(H),nl,
	showBoard(T).
printHelp :-
	nl,write('Left: h/a, Down: j/s, Up: k/w, Right: l/d, Show board: b, Quit: q'),nl.
printNumber(N) :-
	N >= 1000,
	write(' '),write(N).
printNumber(N) :-
	N >= 100,
	write('  '),write(N).
printNumber(N) :-
	N >= 10,
	write('   '),write(N).
printNumber(N) :-
	N == 0,
	write('    _').
printNumber(N) :-
	write('    '),write(N).
pyLeft(Board, NewBoard) :-
    board(Board),
    once(moveLeft(Board, NewBoard)).