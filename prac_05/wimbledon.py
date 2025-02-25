"""
Estimate: 40 minutes
Actual: 45 minutes
"""

filename = "wimbledon.csv"

def main():
    """Process and display Wimbledon champion data"""
    champions_data = read_data(filename)
    champion_count = count_champions(champions_data)
    countries = get_countries(filename)

    print("Wimbledon Champion")
    for champion, wins in champion_count.items():
        print(f"{champion} {wins}")

    print("\nThese countries have won Wimbledon: ")
    print(",".join(sorted(countries)))

def read_data(filename):
    """Read data and returns a list of champions"""
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [
            line.strip().split(',')[2]
            for line in file if not line.startswith('Year')
        ]

def count_champions(champions_data):
    """Count how many times each champion has won"""
    return {champion: champions_data.count(champion)
            for champion in set(champions_data)}

def get_countries(filename):
    """Return a sorted list of countries that have had a champion"""
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            if not line.startswith('Year'):
                countries.add(line.split(',')[1].strip())
    return countries

main()

