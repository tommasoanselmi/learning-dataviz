from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60, 40, 30, 20]
labels = ['Label 1', 'Label 2', 'Label 3', 'Label 3']
explode = [0, 0, 0.1, 0]

plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, explode=explode, startangle=35, autopct='%1.1f%%')

plt.title("Pie")
plt.tight_layout()
plt.show()