# Rock-Paper-Scissors-2

# Activity 4

# Using Loops:

# Enhance the previously written Rock-Paper-Scissors code so that it asks the user if they want to play another round.
# If they say 'Yes', the game should begin again.
# If they say 'No', the game should exit.

user1 = input("What is Player 1's name? ")
user2 = input("What is Player 2's name? ")


user1_answer = input(user1 + ", do you want to choose rock, paper or scissors? ").lower()
user2_answer = input(user2 + ", do you want to choose rock, paper or scissors? ").lower()


if user1_answer == user2_answer:
    print("It's a tie!")
elif user1_answer == 'rock':
    if user2_answer == 'scissors':
        print("Rock wins!")
    else:
        print("Paper wins!")
elif user1_answer == 'scissors':
    if user2_answer == 'paper':
        print("Scissors win!")
    else:
        print("Rock wins!")
elif user1_answer == 'paper':
    if user2_answer == 'rock':
        print("Paper wins!")
    else:
        print("Scissors win!")
else:
    print("Invalid input! try again.")
while True:
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again == 'yes':
        user1_answer = input(user1 + ", do you want to choose rock, paper or scissors? ").lower()
        user2_answer = input(user2 + ", do you want to choose rock, paper or scissors? ").lower()

        if user1_answer == user2_answer:
            print("It's a tie!")
        elif user1_answer == 'rock':
            if user2_answer == 'scissors':
                print("Rock wins!")
            else:
                print("Paper wins!")
        elif user1_answer == 'scissors':
            if user2_answer == 'paper':
                print("Scissors win!")
            else:
                print("Rock wins!")
        elif user1_answer == 'paper':
            if user2_answer == 'rock':
                print("Paper wins!")
            else:
                print("Scissors win!")
        else:
            print("Invalid input! try again.")
    elif play_again == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")