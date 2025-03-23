import datetime


class Project:
    """Represents a project with a name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a formatted string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def is_completed(self):
        """Return True if the project is completed."""
        return self.completion_percentage == 100

    def update(self, completion_percentage=None, priority=None):
        """Update the project's completion percentage and/or priority."""
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if priority is not None:
            self.priority = priority

    @staticmethod
    def from_file_line(line):
        """Create a Project instance from a line of the data file."""
        name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
        return Project(name, start_date, priority, cost_estimate, completion_percentage)
