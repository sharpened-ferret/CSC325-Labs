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

% det.
det(det(Word), [{lex(Word, det, Plurality)} | A], A, Plurality).
% n.
n(n(Word), [{lex(Word, noun, Plurality)}| A], A, Plurality).
% v.
v(v(Words), [{lex(Word, verb, Plurality)} | A], A, Plurality).

lex(the, det, _).
lex(a, det, singular).
lex(man, noun, singular).
lex(men, noun, plural).
lex(woman, noun, singular).
lex(women, noun, plural).
lex(hires, verb, singular).
lex(hire, verb, plural).
lex(falls, verb, singular).
lex(fall, verb, plural).