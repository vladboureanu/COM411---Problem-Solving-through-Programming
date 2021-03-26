#Initialise a set
colours = set()
print(type(colours))


#initialise non empty set
colors = {"blue", "red", "yellow"}


#Adding element to a set
colors.add("purple")
colours.add("red")
colours.add("black")
colours.add("green")

print(colours)
print(colors)


#Union - joining
set1 = colours.union(colors)
print(set1)


#Intersection - finding common elements
set2 = colours.intersection(colors)
print(set2)