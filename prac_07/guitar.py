class Guitar:
    """Represents a guitar with a name,year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Calculate and return the age of the guitar."""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 years or older), otherwise False."""
        return self.get_age() >= 50

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Define the less-than operator for sorting guitars by year"""
        return self.year < other.year
