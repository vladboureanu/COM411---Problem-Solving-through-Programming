<<<<<<< HEAD
#Define an empty list
fruits = []

#Define a list with items
vegetables = ["Carrot", "Peas"]

#Add items to the list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tomatoe")
fruits.append("Banana")

print(fruits)

#Remove an item from a list
fruits.remove("Banana")

print(fruits)

#Remove item from index
del fruits[1]
print(fruits)

#Insert a value not at the end
fruits.insert(1, "Pineapple")
print(fruits)

#Access single element
print(fruits[0])
=======
def isPrime(x):
  for i in range(2,x):
    if x%i == 0:
      return False
  return True

def findPrime(beginning, finish):
  for j in range(beginning,finish):
    if isPrime(j):
      return j

def encrypt():
  print("Provide two integers")
  x = int(input())
  y = int(input())
  prime1 = findPrime(x,y)
  print("Provide two integers")
  x = int(input())
  y = int(input())
  prime2 = findPrime(x,y)
  return prime1*prime2

print(encrypt(), encrypt())




#print("What is the number?")
#x = int(input())
#if isPrime(x):
 # print(f"The number {x} is prime!")
#else:
  #print("The number was not prime!")
>>>>>>> 4317789c13f47f1b3a79937a2d1bf0116b3f87fa
