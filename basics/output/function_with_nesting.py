#What lies before us?
#a large boulder

#It's time to run!

#The function

def identify():
    #ask user a question
    print("What lies before us?")
    response = input()

    #checking and display message
    if (response == "a large boulder"):
        print("It's time to run!")
    else:
        print("We will be fine")

#call the function

identify()