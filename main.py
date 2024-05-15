import pyttsx3

robo = pyttsx3.init()

print("Welcome to Robot Speaker1.1. Created by sakesh")

while True:
  user_input =input("Enter what you wnat robot to speak or enter 0 to exit : ")
  if user_input == "0":
    break
  else:
    print(user_input)
    robo.say(user_input)
    robo.runAndWait()