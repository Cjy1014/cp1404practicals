"""
Name: Jingyang Cai
Date started: 24/2/2025
GitHub URL: https://github.com/Cjy1014/cp1404practicals/tree/prac_05-feedback/Assessment%201
"""


def main():
    """..."""
    print("Song List 1.0 - by Your Name")

def mark_song_learned(songs):
    """Mark an unlearned song as learned."""
    unlearned_songs = [song for song in songs if song[3] == "u"]

    if not unlearned_songs:
        print("No more songs to learn!")
        return

    valid_selection = False
    while not valid_selection:
        try:
            num = int("Enter the number of a song to mark as learned. ") - 1
            if 0 <= num < len(songs) and songs[num][3] == "u":
                songs[num][3] = "l"
                print(f"{songs[num][0]} by {songs[num][1]} marked as learned!")
                valid_selection = True
            else:
                print("Invalid input or song already learned.")
        except ValueError:
            print("Please enter a valid integer.")


def save_songs(filename, songs):
    """Save song to a CSV file."""
    with open(filename, "W") as file:
        for song in songs:
            file.write(",".join(map(str, song)) + "\n")
        print(f"f{len(songs)} songs saved to {filename}.")


if __name__ == '__main__':
    main()