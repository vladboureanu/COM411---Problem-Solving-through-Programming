import matplotlib.pyplot as plt
x = ["Baby", "Todler", "Teen", "Adult"]
y = [10,15,18,20]

plt.xlabel("Age")
plt.ylabel("Height")

plt.bar(x,y, color = ["m", "g", "r", "b"])
plt.plot(x,y)

plt.show()