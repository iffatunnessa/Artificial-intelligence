:- dynamic t_node/2.

t_node(i, nil).
t_node(a, i).
t_node(b, i).
t_node(d, b).
t_node(e, b).
t_node(f, b).
t_node(g, e).

:- dynamic t_node/4.

t_node(i, 0, nil, 80).
t_node(a, 1, 0, 90).
t_node(b, 2, 0, 87).

:- dynamic pq/1.

pq([node(b, 2, 0, 87), node(a, 1, 0, 90)]).

:- dynamic pp/1.


