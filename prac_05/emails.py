"""
Estimate: 30 minutes
Actual: 35 minutes
"""

def main():
    email_to_name = {}

    email = input("Email: ").strip()

    while email != '':
        name = get_name_from_email(email)

        confirmation = input(f"Is your name {name}? y/n: ").strip().lower()

        if confirmation == '' or confirmation == 'y':
            email_to_name[email] = name
        else:
            name = input("Name: ").strip()
            email_to_name[email] = name

        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extracts and formats the name from the part before '@' in the email"""
    name_parts = email.split('@')[0]
    name_words = name_parts.split('.')
    formatted_name = ' '.join(word.title() for word in name_words)
    return formatted_name

main()
