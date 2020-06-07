
parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib'). male('Rakib').

father(X,Y):-parent(X,Y).

findf :- write(' Grandchild: '), read(Y), write('Grandfather: '),
		father(X,Y), write(X), tab(5).
findf.
