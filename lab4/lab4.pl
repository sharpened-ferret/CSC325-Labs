% KB:

byCar(auckland,hamilton).
byCar(hamilton,raglan).
byCar(valmont,saarbruecken).
byCar(valmont,metz).

byTrain(metz,frankfurt).
byTrain(saarbruecken,frankfurt).
byTrain(metz,paris).
byTrain(saarbruecken,paris).
           
byPlane(frankfurt,bangkok).
byPlane(frankfurt,singapore).
byPlane(paris,losAngeles).
byPlane(bangkok,auckland).
byPlane(losAngeles,auckland).

% PROBLEM 1:

% Checks individual transport modes, then chains.
travel(X, Y) :- 
    byPlane(X, Y) 
    ; byCar(X, Y) 
    ; byTrain(X, Y)
    ; travel(X, Z), travel(Z, Y).

% QUERIES:

% Can you get from Valmont to Raglan? 
?- travel(valmont,raglan).

% Where can you get from Valmont to? Give the first 9 answers.
/* 10 ?- travel(valmont, X).
X = saarbruecken ;
X = metz ;
X = frankfurt ;
X = paris ;
X = bangkok ;
X = singapore ;
X = auckland ;
X = hamilton ;
X = raglan ; */

% Are there any problems getting further results? Describe the problem.
/* After 9 answers the 1gb stack limit is exceeded due to infinite recursion 
   as the program loops between the same destinations. 
*/

%?- travel(valmont, singapore)
% What are the means of travel; give this as a narrative answer.
/* 
Valmont -> Metz by car, 
Metz -> Frankfurt by train, 
Frankfurt -> Singapore by plane 
*/


% Problem 2

travel(X, Y, go(X, Y)) :-
    byPlane(X, Y) 
    ; byCar(X, Y) 
    ; byTrain(X, Y).

travel(X, Y, go(X, Z, G)) :-
    byTrain(X, Z), travel(Z, Y, G).

travel(X, Y, go(X, Z, G)) :-
    byCar(X, Z), travel(Z, Y, G).

travel(X, Y, go(X, Z, G)) :-
    byPlane(X, Z), travel(Z, Y, G).

% Can you travel from Valmont to Paris via Metz?
?- travel(valmont,paris,go(valmont,metz,go(metz,paris))).

/*
  travel(valmont, losAngeles, X).
*/


% Problem 3

% KB:
directTrain(saarbruecken,dudweiler).
directTrain(forbach,saarbruecken).
directTrain(freyming,forbach).
directTrain(stAvold,freyming).
directTrain(fahlquemont,stAvold).
directTrain(metz,fahlquemont).
directTrain(nancy,metz).

% Write a predicate to represent that where there is a train connection A to B,
% there is also a train connection from B to A.
directTrain(A, B) :- directTrain(B,A).



% Problem 4

/* 
Rules:
1. A and B implies C
2. negation X imples A
3. D and F imples X

Initial Memory:
D = True
F = True
B = True

Hypothesis C:
  C is not in initial memory
  C is the head of rule 1
  New hypothesis for A and B
    B is proven,
    A is not proven
      Therefore C is not proven 

Hypothesis B:
  B is in memory, 
    therefore hypothesis B is proven

Hypothesis A:
  A is not in memory
  A is the head of rule 2
    If Hypothesis \+X then A
      hypothesis \+X is not proven
        therefore A is not proven

Hypothesis \+X:
  X is not in memory
  X is the head of rule 3
  New Hypothesis D and F
  D and F are true, 
    therefore X is true
      therefore \+X is not proven

Hypothesis D:
  D is in memory
    therefore hypothesis D is proven

Hypothesis F:
  F is in memory
    Therefore F is proven

  

*/