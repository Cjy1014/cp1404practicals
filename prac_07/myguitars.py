from guitar import Guitar

filename = 'guitar.csv'

def main():
    guitars = read_guitars_from_file(filename)

    display_guitars(guitars)

    sort_and_display_guitars(guitars)

    new_guitar = get_new_guitar_from_user()
    guitars.append(new_guitar)

    write_guitars_to_file(filename, guitars)

    print("\nNew guitar added:")
    print(new_guitar)

def read_guitars_from_file(filename):
    """Read guitar data from the file and return a list of guitar objects"""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def write_guitars_to_file(filename, guitars):
    """Write the guitar data to the file"""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def get_new_guitar_from_user():
    """Get new guitar information from the user"""
    name = input("Enter the guitar name: ")
    year = int(input("Enter the guitar year: "))
    cost = float(input("Enter the guitar cost: $"))
    return Guitar(name, year, cost)


def display_guitars(guitars):
    """Display all guitar information"""
    print("All guitars:")
    for guitar in guitars:
        print(guitar)


def sort_and_display_guitars(guitars):
    """Sort the guitars by year and display them"""
    guitars.sort()
    print("\nSorted guitars by year:")
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
