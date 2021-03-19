def get_fruits():
  fruits = []
  print("How many fruits would you like to enter?")
  n = int(input())
  for i in range(4):
    print("Type in the next fruit:")
    fruits.append(input())
  print("Your fruits are {}".format(fruits))

get_fruits()