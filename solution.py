from cmath import sqrt as s
from math import sqrt as sq
print("enter coefficients..")
a ,b,c= float(input("a: ")), float(input("b:")),float(input("c:"))

d= b**2 - 4*a*c
print(d)
if d==0:
	print("There is one root:",-b/(2*a))
elif d>0:
	r1 = (((-b) + sq(d))/(2*a))     
	r2 = (((-b) - sq(d))/(2*a))
	print("There are 2 real roots: {} and {}".format(r1,r2))
else:
	r1 = (((-b) + s(d))/(2*a))     
	r2 = (((-b) - s(d))/(2*a))
	print("There are 2 imaginary roots: {} and {}".format(r1,r2))