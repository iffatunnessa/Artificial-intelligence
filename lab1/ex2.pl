Parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib'). parent('Hasib','Rima'). parent('Hasib','Rahim'). male('Hasib'). male('Rakib'). male('Rashid'). male('Sohel').  male('Rahim').

brother(X,Y):-parent(Z,X), parent(Z,Y), male(X), not(X=Y).
sister(X,Y):-parent(Z,X), parent(Z,Y), not(male(X)).
aunt(A,X):-parent(Z,X), parent(Y,Z), parent(Y,A), not(male(A)).
uncle(U,X):-parent(Z,X), parent(Y,Z), parent(Y,U), male(U), not(Z=U).



findb :- write(' Brother of: '), read(Y), write(' '),
		brother(X,Y), write(X), tab(5), fail.
findb.

finds :- write(' Sister of: '), read(Y), write(' '),
		sister(X,Y), write(X), tab(5), fail.
finds.

finda :- write(' Aunt of: '), read(Y), write(' '),
		aunt(X,Y), write(X), tab(5), fail.
finda.

findu :- write(' Uncle of: '), read(Y), write(' '),
		uncle(X,Y), write(X), tab(5), fail.
findu.
