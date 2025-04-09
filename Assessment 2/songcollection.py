"""SongCollection class for CP1404 Assignment 2
Author: <Jingyang Cai>
Date: <09/04/2-25>
"""

import json
from song import Song


class SongCollection:
    """Represent a collection of song objects."""

    def __init__(self):
        """Initialize a collection with an empty list."""
        self.songs = []

    def add_song(self, song):
        """Add a song to the collection."""
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        """Return the number of songs not learned."""
        return sum(not song.is_learned for song in self.songs)

    def get_number_of_learned_songs(self):
        """Return the number of songs learned."""
        return sum(song.is_learned for song in self.songs)

    def load_songs(self, filename):
        """Load songs from a JSON file."""
        with open(filename, 'r', encoding='utf-8') as in_file:
            data = json.load(in_file)
            self.songs = [Song(*item) for item in data]

    def save_songs(self, filename):
        """Save songs to a JSON file."""
        with open(filename, 'w', encoding='utf-8') as out_file:
            json.dump([[s.title, s.artist, s.year.is_learned] for s in self.songs], out_file, indent=4)

    def sort(self, key):
        """Sort the collection by given key, then by title."""
        self.songs.sort(key=lambda s: (getattr(s, key), s.title))

