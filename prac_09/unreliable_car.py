import random
from car import Car

class UnreliableCar(Car):
    """A car that only sometimes drives, based on its reliability."""

    def __init__(self, make, fuel, reliability):
        """Initialise an UnreliableCar with given reliability."""
        super().__init__(make, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive only if a random number is within reliability percentage."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
