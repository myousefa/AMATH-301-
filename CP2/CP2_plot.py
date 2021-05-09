import numpy as np
import matplotlib.pyplot as plt

def dds(r:float,x0:float,n:int):
    data = []
    xn = x0
    for i in range(n):
        x = r * xn * (1 - xn)
        data.append(x)
        xn = x
    row = np.array(data) # shape (100,)
    col = np.reshape(row, (1,100))
    return row,col

A11_row,A11 = dds(r=2.75,x0=0.2,n=100)
behavior = 1
x_std = np.std(A11)
### Do the same as above except for A13 and A14

A13_row,A13 = dds(r=3.25,x0=0.2,n=100)
behavior = 2
x_std = np.std(A13)
### Do the same as above except for A15 and A16
A15_row,A15 = dds(r=3.75,x0=0.2,n=100)
behavior = 3
x_std = np.std(A15)

def plot_pop(row):
  time = np.arange(len(row))

  plt.plot(time,row)
  plt.show()

plot_pop(A11_row)

A13_row,A13 = dds(r=3.25,x0=0.2,n=100)
plot_pop(A13_row)

A15_row,A15 = dds(r=3.75,x0=0.2,n=100)
plot_pop(A15_row)