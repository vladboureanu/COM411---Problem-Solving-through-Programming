phonebook = {}

<<<<<<< HEAD
while True:
  name = input("Enter the name: ")
  number = input("Enter the number: ")
  phonebook[name] = number
  if input("Type 'x' to stop") == 'x':
    break

def calling(n, book = {}):
  print(f"Calling {n} with a phone number {book[n]}")
=======
    for count in range(5):
        print("Please enter an observation: ")
        observations.append(input())

    return observations
>>>>>>> 1c2f70e0de405d9d6a6dbee651658ce4d2a75951

phonebook["Tadek"] = "12343214234"

<<<<<<< HEAD
calling("vlad", phonebook)
=======
    while(is_running):
        print("Do you wish to remove an observation (yes/no)?")
        response = input()

        if (response == "yes"):
            print("Enter the observation you wish to remove")
            observation = input()
            observations.remove(observation)
        else:
            is_running = False

def run():
    observations = observed()
    remove_observations(observations)

    #populate the set
    observations_set = set()
    for observation in observations:
        data = (observations, observations.count(observation))
        observations_set.add((data))

    #display the set that we have
    for data in sorted(observation_set):
        print(f"{data[0]} {data[1]}")
run()
>>>>>>> 1c2f70e0de405d9d6a6dbee651658ce4d2a75951
