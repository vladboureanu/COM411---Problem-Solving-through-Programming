import matplotlib.pyplot as plt

x = ("Lithuania", "Romania", "Poland", "Bangladesh", "Brazil", "Colombia", "Others")

data = [2,17,1,2,2,2,6]

plt.pie(data, labels = x,  explode = [0.01,0.02,0.03,0.04,0.05,0.06,0.07])

plt.show()