import random

# to loop the game after each by asking the player if they would like to play again after each round, we will have to add a while loop here
while True: 
# creating the list of choices for the game
    choices = ["rock", "paper", "scissors"]

# setting a random choice for computer choice from the list of choices
    computer_choice = random.choice(choices)

# setting player choice
    player_choice = input("rock, paper or scissors? ").lower()

# controlling the input entered by the player to loop if the player choice is not in chpices
    while player_choice not in choices:
        print("invalid input!")
        player_choice = input("rock, paper or scissors? ").lower()

# declaring a winner from the player and computer choice
    if player_choice == computer_choice:
    # printing out the computer and player choices
        print("computer chose: ", computer_choice)
        print("player chose: ", player_choice)
        print("Tie!")

    elif player_choice == "rock":
    # here we will use a nested if in the elif to determine the winner when player picks rock
        if computer_choice == "scissors":
            print("computer chose: ", computer_choice)
            print("player chose: ", player_choice)
            print("You win!")
        if computer_choice == "paper":
            print("computer chose: ", computer_choice)
            print("player chose: ", player_choice)
            print("You lose!")

    elif player_choice == "paper":
        if computer_choice == "rock":
            print("computer chose: ", computer_choice)
            print("player chose: ", player_choice)
            print("You win!")
        if computer_choice == "scissors":
            print("computer chose: ", computer_choice)
            print("player chose: ", player_choice)
            print("You lose!")

    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("computer chose: ", computer_choice)
            print("player chose: ", player_choice)
            print("You win!")
        if computer_choice == "rock":
            print("computer chose: ", computer_choice)
            print("player chose: ", player_choice)
            print("You lose!")

# we will store the input in a variable so we can use it in the if condition for the looping of the game where we will state that if play again is not equal to yes then we will have to break out from the loop
    play_again = input("Would you like to play again? (yes,no) ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")


