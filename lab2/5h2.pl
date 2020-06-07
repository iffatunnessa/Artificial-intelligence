gtp(1,1,1). gtp(2,1,2). gtp(3,1,3). gtp(4,2,3). gtp(5,3,3). gtp(6,3,2). gtp(7,3,1). gtp(8,2,1). gblnk(2,2).



tp(1,1,2). tp(2,1,3). tp(3,2,1). tp(4,2,3). tp(5,3,3). tp(6,2,2). tp(7,3,2). tp(8,1,1). blnk(3,1).

go:- catcH(1,[],L), sum(L,V), write('h2: '), write(V).

catcH(9,X,X):-!.
catcH(T,X,Y):- dist(T,D), append(X,[D],X1), T1 is T+1, catcH(T1,X1,Y).
dist(T,V):- tp(T,A,B), gtp(T,C,D), V is abs(A-C)+abs(B-D).
sum([],0):-!.
sum(L,V):-L=[H|T], sum(T,V1), V is V1+H.
