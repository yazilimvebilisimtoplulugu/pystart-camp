A={"football", "chess"}
B={"music", "chess"}
print( A & B)
print( A - B)
print( B - A)
print(A | B)
o= not A.isdisjoint(B)
print(o)
k=len(A)==len(B)
print(k)
k1=len(A)>=3 and len(B)>=3
print(k1)
k2= ("chess" in A)and("chess" in B)
print(k2)