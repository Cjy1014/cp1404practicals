from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A fancy taxi service with additional cost scaling and flagfall charge."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi with a fanciness multiplier."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate fare including flagfall charge, rounded to nearest 10 cents."""
        return round(super().get_fare() + self.flagfall, 1)

    def __str__(self):
        """Return a string representation of SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
