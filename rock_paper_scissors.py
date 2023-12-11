import random

user_selection = input("Rock, Paper or Scissors? \nPlease make your choice : ")
choice = ["Rock", "Paper", "Scissors"]
if user_selection not in choice:
    print("You entered an incorrect value")
    exit()

random_item = random.choice(choice)
print(f"You chose: {user_selection} and Computer chose: {random_item}")

if user_selection == random_item:
    print("It's a draw!")
elif user_selection == "Rock" and random_item == "Scissors":
    print("It's a win!")
elif user_selection == "Scissors" and random_item == "Paper":
    print("It's a win!")
elif user_selection == "Paper" and random_item == "Rock":
    print("It's a win!")
else:
    print("It's a loss!")
