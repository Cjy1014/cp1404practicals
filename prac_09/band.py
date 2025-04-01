class Band:
    """Band class that contains a list of Musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band, listing its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a Musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument or needing one."""
        return "\n".join(musician.play() for musician in self.musicians)


if __name__ == "__main__":
    from musician import Musician
    from guitar import Guitar

    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
    band.add(nuno)
    band.add(Musician("Gary Cherone"))
    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.add(pat)
    kevin = Musician("Kevin Figueiredo")
    band.add(kevin)

    print("band (str)")
    print(band)
    print("band.play()")
    print(band.play())
