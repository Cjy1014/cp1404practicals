"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song("", "", 0)
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert default_song.is_learned is False

    # Test initial-value song
    print("\nTest initial-value song: ")
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    assert initial_song.title == "My Happiness"
    assert initial_song.artist == "Powderfinger"
    assert initial_song.year == 1996
    assert initial_song.is_learned is True

    #Test mark_learned method
    print("\nTest mark_learned: ")
    initial_song.mark_learned = True
    assert initial_song.is_learned is True
    assert str(initial_song).endswith("(learned)")

    print("\nAll test passed.")


run_tests()
