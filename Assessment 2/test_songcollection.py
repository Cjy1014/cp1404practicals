"""Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection


def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print("Songs:", song_collection.songs)
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs
    print("\nTest loading songs:")
    song_collection.load_songs('songs.json')
    print("Loaded songs count:", len(song_collection.songs))
    assert song_collection.songs  # assuming file is non-empty, non-empty list is considered True

    # Test adding a new Song with values
    print("\nTest adding new song:")
    new_song = Song("My Happiness", "Powderfinger", 1996, True)
    song_collection.add_song(new_song)
    print("Last song in collection:", song_collection.songs[-1])
    assert song_collection.songs[-1].title == "My Happiness"

    # Test sorting songs
    print("\nTest sorting - by year:")
    song_collection.sort("year")
    print("First song after sort by year:", song_collection.songs[0])

    print("\nTest sorting - by artist:")
    song_collection.sort("artist")
    print("First song after sort by artist:", song_collection.songs[0])

    print("\nTest count learned/unlearned:")
    learned = song_collection.get_number_of_learned_songs()
    unlearned = song_collection.get_number_of_unlearned_songs()
    print(f"Learned: {learned}, Unlearned: {unlearned}")
    assert learned + unlearned == len(song_collection.songs)

    print("\nTest saving songs to test_output.json (check manually):")
    song_collection.save_songs('test_output.json')

    print("\nAll SongCollection tests passed.")


run_tests()