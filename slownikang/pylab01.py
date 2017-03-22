import pylab
import numpy as np

a = int(raw_input("podaj a: "))
b = int(raw_input("podaj b: "))

x = np.arange(-10,11,0.5)

y1 = [(x1/(-3)) + a for x1 in x if x1 <= 0]
y2 = [(x2 * x2/(3)) for x2 in x if x2 >= 0]
print x
print y1
print y2

pylab.plot(x[:len(y1)],y1)
pylab.plot(x[-len(y2):],y2)
pylab.title("wykres f(x) = ax + b")
pylab.grid(True)
pylab.show()
