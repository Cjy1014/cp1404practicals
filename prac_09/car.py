class Car:
    """A simple Car class."""

    def __init__(self, name, fuel):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def drive(self, distance):
        """Drive the car a given distance if it has enough fuel."""
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance

        self.odometer += distance_driven
        return distance_driven
