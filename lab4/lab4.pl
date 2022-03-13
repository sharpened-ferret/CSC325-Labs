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


