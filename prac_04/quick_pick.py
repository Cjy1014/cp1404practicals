import random

NUMBERS = list(range(1, 46))

def main():
    num_picks = int(input("How many quick picks? "))
    generate_quick_picks(num_picks)

def generate_quick_picks(num_picks):
    """Generate the specified number of 'quick pick' random numbers."""
    for i in range(num_picks):
        quick_pick = random.sample(NUMBERS, 6)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))

main()