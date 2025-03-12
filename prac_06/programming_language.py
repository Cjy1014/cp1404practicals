"""
Estimate time: 20 minutes
Actual time: 26 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

        def is_dynamic(self):
            """Return True if this language is a dynamically typed, otherwise False."""
            return self.typing.lower() == "dynamic"

        def __str__(self):
            """Return a string representation of the programming language."""
            return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
