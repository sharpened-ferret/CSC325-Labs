% % s --> np,vp.
% s(s(A, C), A, C) :-
%     np(A, A, B),
%     vp(c, B, C).

% % np --> det,n.
% np(np(A, B), A, B) :-
%     det(A, A, B),
%     n(B, B).

% % vp --> v,np.
% vp(vp(v(A), np(C)), A, C) :-
%     v(A, A, B),
%     np(C, B, C). 

% % det --> [the].
% det(det(A), [the | A], A).
% % det --> [a].
% det(det(A), [a | A], A).
% % n --> [woman].
% n(n(A), [woman| A], A).
% % n --> [man].
% n(n(A), [man | A], A).
% % v --> [hire].
% v(v(A), [hire | A], A).


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
v([hire | A], A).