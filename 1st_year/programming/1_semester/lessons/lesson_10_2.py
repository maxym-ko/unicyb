import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return res[0] * x + res[1]


data = np.array([(6, 100), (14, 150), (18, 200), (20, 250), (22, 300), (23, 350)])

data_x = []
data_y = []

for el in data:
    data_x.append(el[0])
    data_y.append(el[1])

x = np.vstack((np.asarray(data_x), np.ones(len(data_x))))

a = x @ x.T
b = x @ data_y

res = b @ np.linalg.inv(a)

print(res)

x = np.linspace(0, 50, 100)
y = f(x)

plt.plot(x, y)
for el in data:
    plt.scatter(el[0], el[1])
plt.show()
