# ask a user what to do
print("What should I do (play/study)?")
activity = input()

# decide if Beep should play or study
if (activity == "play"):

  # ask a user to play with
  print("What sould I play with (toy/friends)?")
  play_with = input()

  #decide if Beep should play with toys or friends
  if(play_with == "toy"):
    print("I will play with my toys!")
  else:
    print("I will play with my friends!")
  
else:
  print("I will study!")