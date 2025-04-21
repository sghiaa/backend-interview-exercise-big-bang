import random
import json
import os

RULES = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}

CHOICES = list(RULES.keys())
SCORE_FILE = "scoreboard.json"

def load_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return default_score()

def save_score(score):
    with open(SCORE_FILE, "w") as f:
        json.dump(score, f, indent=2)

def default_score():
    return {
        "You": {"wins": 0, "losses": 0, "ties": 0},
        "Computer": {"wins": 0, "losses": 0, "ties": 0},
    }

def reset_score():
    score = default_score()
    save_score(score)
    print_score(score)
    print("Scoreboard has been reset.")
    return score

def print_score(score):
    print("\n🏆 Scoreboard:")
    for player, stats in score.items():
        print(f"{player}: {stats['wins']} Wins | {stats['losses']} Losses | {stats['ties']} Ties")

def get_user_choice():
    print("\nPlayer, choose one:")
    for i, choice in enumerate(CHOICES, 1):
        print(f"{i}. {choice.capitalize()}")
    while True:
        try:
            selection = int(input("Your choice (1-5): "))
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
        return "player"
    else:
        return "computer"

def play_round():
    player_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice.capitalize()}")

    winner = determine_winner(player_choice, computer_choice)

    return {
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "winner": winner
    }

def main():
    print("Welcome to Rock Paper Scissors Lizard Spock!")
    score = load_score()

    while True:
        print("\nWhat would you like to do?")
        print("1. Play a round")
        print("2. View scoreboard")
        print("3. Reset scoreboard")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            result = play_round()
            winner = result["winner"]
            if winner == "tie":
                print("It's a tie!")
                score["You"]["ties"] += 1
                score["Computer"]["ties"] += 1
            elif winner == "player":
                print("You win!")
                score["You"]["wins"] += 1
                score["Computer"]["losses"] += 1
            else:
                print("You lose!")
                score["You"]["losses"] += 1
                score["Computer"]["wins"] += 1
            save_score(score)

        elif choice == "2":
            print_score(score)

        elif choice == "3":
            score = reset_score()

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
