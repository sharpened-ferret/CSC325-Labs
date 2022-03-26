% s --> foo,bar,wiggle.
s(A, D) :-
    foo(A, B),
    bar(B, C),
    wiggle(C, D).

% foo --> [choo].
foo([choo | A], A).

%foo --> foo,foo.
foo(A, C) :-
    foo(A, B),
    foo(B, C).

% bar --> mar,zar.
bar(A, C) :-
    mar(A, B),
    zar(B, C).

% mar --> me,my.
mar(A, C) :-
    me(A, B),
    my(B, C).

% me --> [i].
me([i | A], A).

% my --> [am].
my([am | A], A).

% zar --> blar,car.
zar(A, C) :-
    blar(A, B),
    car(B, C).

% blar --> [a].
blar([a | A], A).

% car --> [train].
car([train | A], A).

% wiggle --> [toot].
wiggle([toot | A], A).

% wiggle --> wiggle,wiggle.
wiggle(A, C) :-
    wiggle(A, B),
    wiggle(B, C).

% X = [choo, i, am, a, train, toot] ;
% X = [choo, i, am, a, train, toot, toot] ;
% X = [choo, i, am, a, train, toot, toot, toot] ;

