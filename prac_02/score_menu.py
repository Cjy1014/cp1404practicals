def main():
    """Handle user choices."""
    score = get_valid_score()

    display_menu()
    choice = input("Enter choice: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice! Please try again.")

        display_menu()
        choice = input("Enter choice: ").upper()

    print("Goodbye!")


def get_valid_score():
    """Prompt the user to enter a valid score (0-100 inclusive)."""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Try again.")
        score = float(input("Enter a valid score (0-100): "))
    return score

def get_score_result(score):
    """Determine the result based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print as many stars as the score."""
    print("*" * int(score))

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

main()