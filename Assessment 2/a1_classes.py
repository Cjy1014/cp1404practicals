"""
Author: <Jingyang Cai>
Date: <10/04/2-25>
"""

from songcollection import SongCollection
from song import Song


FILENAME = "songs.json"


def main():
    """Console interface for Song List 2.0 using Song and SongCollection classes."""
    print("Song List 2.0 - by Your Name")

    songs = SongCollection()
    songs.load_songs(FILENAME)
    print(f"{len(songs.songs)} songs loaded from {FILENAME}")

    # Display all songs
    for i, song in enumerate(songs.songs):
        mark = "*" if not song.is_learned else " "
        print(f"{mark} {i}. {song}")

    # Mark song as learned
    mark_song_learned(songs)

    # Save and exit
    songs.save_songs(FILENAME)
    print(f"{len(songs.songs)} songs saved to {FILENAME}")


def mark_song_learned(song_collection):
    """Mark an unlearned song as learned."""
    unlearned = [song for song in song_collection.songs if not song.is_learned]

    if not unlearned:
        print("No more songs to learn!")
        return

    try:
        num = int(input("Enter the number of a song to mark as learned: "))
        song = song_collection.songs[num]
        if song.is_learned:
            print("You have already learned this song.")
        else:
            song.mark_learned()
            print(f"{song.title} by {song.artist} learned.")
    except (ValueError, IndexError):
        print("Invalid input.")


if __name__ == "__main__":
    main()
