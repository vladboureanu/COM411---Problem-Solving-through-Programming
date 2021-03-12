#escape_by("jumping over")
#escape_by("jumping around")
#escape_by("going deeper")

#we cannot escape that way! The boulder is too big!
#we cannot escape that way! The boulder is moving too fast!
#That my work! let's go deeper!


#This is function with single plan and name is 'plan'

def escape_by(plan):
    if(plan == "jumping over"):
        print("We cannot escape that way! The boulder is too big!")
    elif(plan == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif(plan == "going deeper"):
        print("That my work! let's go deeper!")
    else:
        print("Not sure about this plan")

#call the function

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("let's listen")