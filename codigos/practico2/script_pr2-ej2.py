from math import tan
import matplotlib.pyplot as plt
from funciones.biseccion import rbisec

fun = lambda x: x**2

#def fun(x):
#	return 2*x - tan(x)

I = [0.8, 1.4]
#hx, hf = rbisec(fun, I, 100, 10**(-5))

#print(hx)

x = []
for i in range(100):
	x.append(2*(i/100)+0.1)
print(x, "\n")

#x_ = [2*(a/100)+0.1  for a in range(100)]
#print(x_)
 

y = [fun(i) for i in x]
print(y)

plt.plot(x, y, '.r')
plt.show()


