#Program that displays a menu and allows the user to either see a nice message, calculate area of rectangle or triangle or diplays a times table for a number

print("Please choose and option from the menu:\n1-Nice message\n2-Area of a rectangle\n3-Area of a triangle\n4-Times table")

option = int(input())

if option == 1:
  print("Today will be a good day!")
elif option == 2:
  print("Enter the length of the rectangle:")
  l = int(input())
  print("Enter the width of a rectangle")
  w = int(input())
  area = l*w
  print("The area of this rectangle was {}".format(area))
elif option == 3:
  print("Enter the base of the triangle:")
  b = float(input())
  print("Enter the height of the trianglee")
  h = float(input())
  area = 0.5*b*h
  print("The area of this triangle was {:.2f}".format(area))
elif option == 4:
  print("What number would you like to see the times tbale for?")
  n = int(input())
  for i in range(1,11,1):
    print("{}x{} = {}".format(n,i,n*i))
else:
    print("There is no such option. Go to Specsavers!")