import re

# Function to generate email addresses
def generate_email(name, domain='gmail.com'):
    # Split the name into parts using a comma as the delimiter
    name_parts = name.split(', ')

    # Handle cases where there is only one name or no comma in the name
    if len(name_parts) == 1:
        name_parts = name.split(' ')

    # Extract the surname and the first letter of the second name (if available)
    surname = name_parts[0]
    second_name = name_parts[1][0] if len(name_parts) > 1 else ''

    # Remove special characters and spaces from the names
    surname = re.sub(r'[^a-zA-Z\s]', '', surname)
    second_name = re.sub(r'[^a-zA-Z\s]', '', second_name)

    # Generate the email address
    email = second_name.lower() + surname.lower() + '@' + domain
    return email

# Function to check for special characters in a name with a comma
def has_special_characters_with_comma(name):
    if ',' in name:
        name_without_comma = name.split(', ')[1]  # Extract the part after the comma
        return bool(re.search(r'[^a-zA-Z\s]', name_without_comma))
    return False
