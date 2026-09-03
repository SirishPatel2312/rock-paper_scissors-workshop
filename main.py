import random


CHOICES = ("rock", "paper", "scissors")


def determine_winner(player_choice, computer_choice):
    """Return the result of one round from the player's perspective."""
    invalid_choices = [
        choice for choice in (player_choice, computer_choice) if choice not in CHOICES
    ]
    if invalid_choices:
        raise ValueError(
            f"Choices must be one of {', '.join(CHOICES)}; got {invalid_choices!r}"
        )

    if player_choice == computer_choice:
        return "draw"

    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if winning_combinations[player_choice] == computer_choice:
        return "win"

    return "lose"


def get_player_choice():
    """Prompt until the player enters a valid choice."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice

        print("Invalid choice. Please enter rock, paper, or scissors.")


def main():
    """Play one round of rock, paper, scissors."""
    player_choice = get_player_choice()
    computer_choice = random.choice(CHOICES)
    result = determine_winner(player_choice, computer_choice)

    print(f"You chose {player_choice}.")
    print(f"The computer chose {computer_choice}.")

    if result == "draw":
        print("It's a draw!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    main()