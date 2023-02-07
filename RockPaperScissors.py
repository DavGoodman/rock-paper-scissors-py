import random
rps = ["rock", "paper", "scissors"]
ties = 0
wins = 0
loses = 0
print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")


while True:
    print(f"Wins: {str(wins)} Loses: {str(loses)} Ties: {str(ties)}")
    r_choice = random.choice(rps)
    p_choice = input("> ").lower()

    if p_choice == r_choice[0]:
        print(f"and your opponent chose... {r_choice}!")
        print("its a tie!")
        ties += 1

    elif p_choice == "r" and r_choice == "paper" or p_choice == "s" and r_choice == "rock" or p_choice == "p" and r_choice == "scissors":
        print(f"and your opponent chose... {r_choice}!")
        loses += 1

    elif p_choice == "r" and r_choice == "scissors" or p_choice == "s" and r_choice == "paper" or p_choice == "p" and r_choice == "rock":
        print(f"and your opponent chose... {r_choice}!")
        print("You win!")
        wins += 1


    elif p_choice == "q":
        break

    else:
        print("please enter a valid input")

input("thanks for playing!")



