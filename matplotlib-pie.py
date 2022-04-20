from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60, 40, 30, 20]
labels = ['Sixty', 'Forty', 'Thirty', 'Twenty']

plt.pie(slices, labels=slices, wedgeprops={'edgecolor': 'black'})

plt.title("Pie")
plt.tight_layout()
plt.show()