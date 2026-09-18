import matplotlib
import matplotlib.pyplot as plt
 
x = [0, 1, 2, 3, 4]
y1 = [0, 10, 20, 25, 30]
y2 = [0, 5, 15, 20, 22]
 
# Single line graph
plt.figure(); plt.xlabel("X Axis"); plt.ylabel("Y Axis");  plt.grid(True)
plt.plot(x, y1, label="Series A", color="blue", marker="o")
plt.title("Single Line Graph")
plt.legend()
plt.show()
plt.plot(x, y1, label="Series A", color="blue", marker="o")
plt.plot(x, y2, label="Series B", color="green", marker="s")
plt.title("Multiple Line Graph")
plt.grid(True)
plt.legend()
plt.show()


 