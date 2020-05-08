print("Welcome to the Letter Counter App")

UserName = input("What is your name: ")

print("Hello " + UserName.title() + "!")
print("I will count the number of times that a specific letter occurs in a message.")

UserMessage = input("Please enter a message: ")
UserMessage = UserMessage.lower()

UserLetter = input("What letter would you like to see the frequency of: ")
UserLetter = UserLetter.lower()

print("The letter " + str(UserLetter) + " occurs " + str(UserMessage.count(UserLetter)) + " times.")
