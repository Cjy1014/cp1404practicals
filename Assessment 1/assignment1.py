"""
Name: Jingyang Cai
Date started: 24/2/2025
GitHub URL:
"""


def main():
    """Allows the user to display, add, mark songs, and save data."""
    FILE_NAME = "songs.csv"
    songs = load_songs(FILE_NAME)

    print("Song List 1.0 - by Your Name")
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


if __name__ == '__main__':
    main()