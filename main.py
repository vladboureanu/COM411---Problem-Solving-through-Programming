<<<<<<< HEAD
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
=======
def display_box(name):
    message = "* Hello {} *".format(name)
    print("*" * len(message))
    print(message)
    print("*" * len(message))

def greet_user():
    print("Please enter your name")
    name=input()
    display_box(name)

greet_user()
>>>>>>> c8daf372391857039f65a30bd821db8dd3e1433d
