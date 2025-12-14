import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Plot")
plt.show()

# Bar chart
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.bar(categories, values)
plt.show()