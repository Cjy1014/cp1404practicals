"""Song class for CP1404 Assignment 2
Author: <Jingyang Cai>
Date: <09/04/2-25>
"""

# TODO: Create your Song class in this file


class Song:
    """Represents a song."""

    def __init__(self, title, artist, year, is_learned=False):
        """Initialize a song instance with title, artist, year, and is learned status."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        """Return string representation of the song."""
        status = "learned" if self.is_learned else "not learned"
        return f"{self.title} - {self.artist} ({self.year}) ({status})"

    def mark_learned(self):
        """Mark the song as learned."""
        self.is_learned = True

    def mark_unlearned(self):
        """Mark the song as unlearned."""
        self.is_learned = False
