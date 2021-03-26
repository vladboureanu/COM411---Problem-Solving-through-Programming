def observed():
    observations = []

    for count in range(5):
        print("Please enter an observation: ")
        observations.append(input())

    return observations

def remove_observations(observations):
    is_running = True

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