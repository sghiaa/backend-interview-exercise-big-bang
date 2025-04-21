import random

RULES = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}

CHOICES = list(RULES.keys())

def get_user_choice(player_name):
    print(f"\n{player_name}, choose one:")
    for i, choice in enumerate(CHOICES, 1):
        print(f"{i}. {choice.capitalize()}")

    while True:
        try:
            selection = int(input(f"{player_name}'s choice (1-5): "))
            if 1 <= selection <= 5:
                return CHOICES[selection - 1]
            else:
                print("Invalid number. Enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(p1, p2):
    if p1 == p2:
        return "tie"
    elif p2 in RULES[p1]:
        return "player1"
    else:
        return "player2"

def play_round(mode): 
    if mode == "1":
        player1 = get_user_choice("You")
        player2 = get_computer_choice()
        print(f"Computer chose: {player2.capitalize()}")
        winner = determine_winner(player1, player2)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player1":
            print("You win!")
        else:
            print("You lose!")

    elif mode == "2":
        player1 = get_user_choice("Player 1")
        print("\n" * 50)  # "Clear" screen between turns
        player2 = get_user_choice("Player 2")

        winner = determine_winner(player1, player2)
        print(f"\nPlayer 1 chose: {player1.capitalize()}")
        print(f"Player 2 chose: {player2.capitalize()}")

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player1":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

def main():
    print("Welcome to Rock Paper Scissors Lizard Spock!")
    print("1. Play against computer")
    print("2. Two-player mode")

    while True:
        mode = input("Choose mode (1 or 2): ").strip()
        if mode in ["1", "2"]:
            break
        else:
            print("Please enter 1 or 2.")

    while True:
        play_round(mode)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
