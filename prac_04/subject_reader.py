FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data_list.append(parts)
    return data_list


def display_subject_details(data):
    """Display subject details in a readable format."""
    for subject in data:
        subject_code, lecturer, num_students = subject
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


main()
