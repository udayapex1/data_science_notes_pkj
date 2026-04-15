# ==================================
# MATPLOTLIB BASICS - SINGLE FILE
# ==================================

import matplotlib.pyplot as plt
import numpy as np

print("===== 1. Basic Line Plot =====")
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


print("===== 2. Multiple Lines =====")
x = np.arange(1, 6)
y1 = x * 2
y2 = x * 3

plt.plot(x, y1, label="y = 2x")
plt.plot(x, y2, label="y = 3x")
plt.legend()
plt.title("Multiple Lines")
plt.show()


print("===== 3. Scatter Plot =====")
x = np.random.randint(1, 50, 20)
y = np.random.randint(1, 50, 20)

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()


print("===== 4. Bar Chart =====")
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()


print("===== 5. Histogram =====")
data = np.random.randn(100)

plt.hist(data, bins=10)
plt.title("Histogram")
plt.show()


print("===== 6. Pie Chart =====")
labels = ["Python", "Java", "C++", "JS"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()


print("===== 7. Subplots =====")
x = np.arange(1, 6)

plt.subplot(1, 2, 1)
plt.plot(x, x**2)
plt.title("x^2")

plt.subplot(1, 2, 2)
plt.plot(x, x**3)
plt.title("x^3")

plt.show()


print("===== 8. Grid & Style =====")
plt.plot(x, x**2)
plt.grid(True)
plt.title("Grid Example")
plt.show()


print("===== 9. Save Figure =====")
plt.plot(x, x)
plt.title("Saved Plot")
plt.savefig("plot.png")  # saves image
plt.show()


print("===== DONE =====")