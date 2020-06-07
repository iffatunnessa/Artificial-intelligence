% Code for generating the successors of a 8-queens' state given as a list of 8 digits
gnrt_sucsr(L):- assert(id(1)), assert(state(1, 'c', L, 50)),
		incr_id, mk_new(1, L), retract(id(_)), evaluate.

incr_id:-id(V), V1 is V+1, retract(id(_)), assert(id(V1)).

mk_new(9, _):-!.
mk_new(N, L):- nthel(N, L, X), del_el(X, [1,2,3,4,5,6,7,8], L1),
		cng_mk(N, L, L1), N1 is N+1, mk_new(N1, L).

cng_mk(_, _, []):-!.
cng_mk(N, L, L1):- L1=[H|T], rplc_nthel(N, H, L, L2), id(Id),    /* id/1 is a dynamic data */
		assert(state(Id, 's', L2, 50)), incr_id, cng_mk(N, L, T).

% Code for determination and display of the best state
checkall:- state(_, 'c', _, V1), threshold(V2), V1 >= V2, I is 1, dsply(I), !.
checkall:- best(I1,V1), threshold(V2), V1 >= V2, I is I1, dsply(I), !.
checkall:- state(_, 'c', _, V1), best(I, V2) ,V2>V1,state(I, _, L, _),
		retractall(state(_, _, _, _)),write_list(['\nIteration max: ', V2]),
		gnrt_sucsr(L), !.
checkall:- restrt, !.

best(I, Max):- state(_, 's', _, Val), assert(max_val(Val)),
		updt_max, max_val(Max), state(I, _, _, Max), retract(max_val(_)), !.

updt_max:- state(_, _, _, V2),  max_val(V1), V2>V1,
		retract(max_val(_)), assert(max_val(V2)), fail.
updt_max:-!.

% Performing Crossover

       go_cross(X,Y,CP):- state(X,'p',L1,_), state(Y,'p',L2,_),CP1 is 8-CP,
	del_1st_n_el(L1,CP,L12),del_last_n_el(L1,CP1,L11),
	del_1st_n_el(L2,CP,L22),del_last_n_el(L2,CP1,L21),
	append(L11,L22,LO1),append(L21,L12,LO2), count_sts(_,N),
	N1 is N+1, N2 is N+2,
	assert(state(N1,'o',LO1,50)), assert(state(N2,'o',LO2,50)).

% Performing Mutation

do_mutn:- count_sts('o',N), N1 is random(N)+1,
		assert(id1(0)),get_offspr(N1,I,T,L,V), retract(id1(_)),
		N2 is random(8)+1, N3 is random(8)+1, rplc_nthel(N2,N3,L,L1),
		retract(state(I,T,L,V)), assert(state(I,T,L1,50)).

get_offspr(N1,I,'o',L,V):- state(I,'o',L,V),incr_id1, id1(N), N1=N,!.
