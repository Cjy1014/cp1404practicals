"""
Estimated Time: 2 hours
Actual Time: 2.5 hours
"""

import datetime
from project import Project

def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    print("Welcome to Pythonic Project Management")
    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to the current file? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option. Please try again.")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            project = Project.from_file_line(line)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save the list of projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display the list of incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda p: p.priority):
        print(project)

    print("\nCompleted projects:")
    for project in sorted(completed_projects, key=lambda p: p.priority):
        print(project)


def filter_projects_by_date(projects, date_str):
    """Filter and display projects that start after the specified date."""
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print(f"New project added: {new_project}")


def update_project(projects):
    """Update the completion percentage and/or priority of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    new_percentage = input(f"New Percentage (current: {project.completion_percentage}): ")
    if new_percentage:
        project.update(completion_percentage=int(new_percentage))

    new_priority = input(f"New Priority (current: {project.priority}): ")
    if new_priority:
        project.update(priority=int(new_priority))

    print(f"Updated project: {project}")


if __name__ == '__main__':
    main()
