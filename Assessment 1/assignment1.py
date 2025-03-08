"""
Name: Jingyang Cai
Date started: 24/2/2025
GitHub URL:
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



if __name__ == '__main__':
    main()