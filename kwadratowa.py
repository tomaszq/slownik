import matplotlib.pyplot as plt

x = xrange(-10,11,1)
print x
a = 1
b = -3
c = 1

y = [a*x1*x1 + b*x1 + c for x1 in x]

plt.plot(x,y)
plt.grid()
plt.title("Wykres f(x) = a*x*x + b*x + c")
plt.show()
