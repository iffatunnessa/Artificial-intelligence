sum1(1,_,F,F):-!.
sum1(N,I,F,S):-N>0, N1 is N-1, sum1(N1,I,F,S1) , S is S1+F+N1*I.

