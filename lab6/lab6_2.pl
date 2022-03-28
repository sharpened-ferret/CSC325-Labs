% ---- Basic Rules ---- %

% s --> np,vp.
s(A, C) :-
    np(A, B),
    vp(B, C).

% np --> det,n.
np(A, C) :-
    det(A, B),
    n(B, C).

% vp --> v,np.
vp(A, C) :-
    v(A, B),
    np(B, C). 

% det --> [the].
det([the | A], A).
% det --> [a].
det([a | A], A).
% n --> [woman].
n([woman| A], A).
% n --> [man].
n([man | A], A).
% v --> [hire].
v([hires | A], A).




% ---- Trace Rules ---- %

% s --> np,vp.
s(s(Tree1, Tree2), A, C) :-
    np(Tree1, A, B),
    vp(Tree2, B, C).

% np --> det,n.
np(np(Tree1, Tree2), A, C) :-
    det(Tree1, A, B),
    n(Tree2, B, C).

% vp --> v,np.
vp(vp(Tree1, Tree2), A, C) :-
    v(Tree1, A, B),
    np(Tree2, B, C). 

% det --> [the].
det(det(the), [the | A], A).
% det --> [a].
det(det(a), [a | A], A).
% n --> [woman].
n(n(woman), [woman| A], A).
% n --> [man].
n(n(man), [man | A], A).
% v --> [hire].
v(v(hires), [hires | A], A).


% --- Tests ---
% s(Tree, [a,man,hires,a,woman],[]).
% s(Tree, [a,woman,hires,the,woman],[]).



% ---- Trace Rules with Quantity ---- %

% s --> np,vp.
s(s(Tree1, Tree2), A, C, Plurality) :-
    np(Tree1, A, B, Plurality),
    vp(Tree2, B, C, Plurality).

% np --> det,n.
np(np(Tree1, Tree2), A, C, Plurality) :-
    det(Tree1, A, B, Plurality),
    n(Tree2, B, C, Plurality).

% vp --> v,np.
vp(vp(Tree1, Tree2), A, C, Plurality) :-
    v(Tree1, A, B, Plurality),
    np(Tree2, B, C, Plurality). 

% det --> [the].
det(det(the), [the | A], A, _).
% det --> [a].
det(det(a), [a | A], A, singular).
%det --> [two].
det(det(two), [two | A], A, plural).
% n --> [woman].
n(n(woman), [woman| A], A, singular).
n(n(women), [women| A], A, plural).
% n --> [man].
n(n(man), [man | A], A, singular).
n(n(men), [men | A], A, plural).
% v --> [hire].
v(v(hires), [hires | A], A, singular).
v(v(hire), [hire | A], A, plural).