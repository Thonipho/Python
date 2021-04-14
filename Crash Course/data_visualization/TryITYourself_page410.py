import matplotlib.pyplot as plt

numbers = range(1,500)
cubes = [x**3 for x in numbers]

fig, ax = plt.subplots()
ax.scatter(numbers,cubes, c=cubes, cmap= plt.cm.Blues, s=10)
plt.show()