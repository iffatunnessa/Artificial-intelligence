
parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib').

grandparent(X,Y):-parent(X,Z), parent(Z,Y).

findGp :- write(' Grandchild: '), read(Y), write('Grandfather: '),
		grandparent(X,Y), write(X), tab(5), fail.
findGp.
