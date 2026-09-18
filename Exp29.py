import matplotlib.pyplot as plt

data = {'A': 30, 'B': 70 ,'C':45,'D':89}
labels, values = list(data.keys()), list(data.values())

plt.figure(figsize=(9, 3))
plt.subplot(131).bar(labels, values, color=['red', 'blue'])       # Vertical Bar
plt.subplot(132).barh(labels, values, color=['green', 'orange'])  # Horizontal Bar
plt.subplot(133).pie(values, labels=labels, autopct='%1.1f%%', colors=['pink', 'cyan','green','red']) # Pie

plt.suptitle(f"Bar and Pie Charts Demo")
plt.show()