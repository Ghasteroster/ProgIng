mark(igor, otl).
mark(mark, troy).
mark(maria, troy).
mark(olga, hor).
student(igor, male).
student(maria, female).
student(mark, male).
student(olga, female).
molodets(X, Y):-student(X, Y), mark(X, hor).
molodets(X, Y):-student(X, Y), mark(X, otl).