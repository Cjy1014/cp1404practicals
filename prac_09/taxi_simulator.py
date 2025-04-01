from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill = 0
    current_taxi = None

    print("Let's drive!")
    while True:
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                bill += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def choose_taxi(taxis):
    """Display available taxis and let user choose one."""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input, please enter a number")
    return None

def drive_taxi(taxi):
    """Prompt user for distance and drive the taxi."""
    try:
        distance = float(input("Drive how far? "))
        taxi.start_fare()
        taxi.drive(distance)
        cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${cost:.2f}")
        return cost
    except ValueError:
        print("Invalid input, please enter a number")
        return 0

def display_taxis(taxis):
    """Display the list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()
