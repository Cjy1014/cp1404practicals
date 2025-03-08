"""
Name: Jingyang Cai
Date started: 24/2/2025
GitHub URL: https://github.com/Cjy1014/cp1404practicals/tree/prac_05-feedback
"""


def main():
    """Allows the user to display, add, mark songs, and save data."""
    FILE_NAME = "songs.csv"
    songs = load_songs(FILE_NAME)

    print("Song List 1.0 - by Jingyang Cai")
    print(f"{len(songs)} songs loaded.\n")

    choice = ""
    while choice != "q":
        print("D - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ").strip().lower()

        if choice == "d":
            display_songs(songs)
        elif choice == "a":
            add_song(songs)
        elif choice == "c":
            mark_song_learned(songs)
        elif choice == "q":
            save_songs(FILE_NAME, songs)
            print("Goodbye!")
        else:
            print("Invalid input, please try again.")


def load_songs(filename):
    """Load song data from a CSV file."""
    songs = []
    try:
        with open(filename, "r") as file:
            for line in file:
                title, artist, year, learned = line.strip().split(",")
                songs.append([title, artist, int(year),learned])
    except FileNotFoundError:
        print("File not found, please create a new file.")
    return songs


def display_songs(songs):
    """Display all songs, sorted by and title, with a count of learned/unlearned songs."""
    songs.sort(key=lambda x: (x[2], x[0]))
    learned_count = sum(1 for song in songs if song[3] == "1")

    for i, song in enumerate(songs, 1):
        marker = "*" if song[3] == "u" else " "
        print(f"{i}. {marker} {song[0]:30} - {song[1]:20} ({song[2]})")

    print(f"\n{learned_count} songs learned, {len(songs) - learned_count} songs still to learn.\n")


def add_song(songs):
    """Add a new song with validated inputs."""
    title = input("Enter song title: ").strip()
    while not title:
        print("Title cannot be empty!")
        title = input("Enter artist name: ").title()

    artist = input("Enter artist: ").strip()
    while not artist:
        print("Artist cannot be empty!")
        artist = input("Enter artist name: ").strip()

    year = None
    while year is None:
        try:
            year_input = input("Enter year: ")
            year = int(year_input)
            if year <= 0:
                print("Year must be greater than 0.")
                year = None
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    songs.append([title, artist, year, "u"])
    print(f"{title} by {artist} ({year}) added to song list.")



if __name__ == '__main__':
    main()