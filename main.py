import random


CHOICES = ("rock", "paper", "scissors")


def get_player_choice():
    """Prompt until the player enters a valid choice."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please choose rock, paper, or scissors.")


def determine_winner(player_choice, computer_choice):
    """Return the result of a round."""
    if player_choice == computer_choice:
        return "It's a tie!"

    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"

    return "Computer wins!"


def main():
    player_choice = get_player_choice()
    computer_choice = random.choice(CHOICES)

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))


if __name__ == "__main__":
    main()
