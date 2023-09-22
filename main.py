import pandas as pd
import re
import openpyxl
import json

# Load the Excel file
file_path = 'testfile.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)

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

# Generate email addresses and store them in a new column
df['Email Address'] = df['Student Name'].apply(generate_email)

# Create separate DataFrames for male and female students
male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']

# Count the number of male and female students
num_male_students = len(male_students)
num_female_students = len(female_students)

# Display the counts
print(f"Number of Male Students: {num_male_students}")
print(f"Number of Female Students: {num_female_students}")

# Function to check for special characters in a name with a comma
def has_special_characters_with_comma(name):
    if ',' in name:
        name_without_comma = name.split(', ')[1]  # Extract the part after the comma
        return bool(re.search(r'[^a-zA-Z\s]', name_without_comma))
    return False

# Create a new column indicating if a student with a comma has special characters in their name
df['Has Special Characters'] = df['Student Name'].apply(has_special_characters_with_comma)

# List the names of students with special characters
students_with_special_chars = df[df['Has Special Characters']]

# Display the names of students with special characters
print("Names of Students with Special Characters:")
for index, row in students_with_special_chars.iterrows():
    print(row['Student Name'])

# Merge all documents into one file
merged_file_path = 'merged_students.xlsx'  # Replace with your desired output file path
df.to_excel(merged_file_path, index=False)

# Shuffle the DataFrame once
shuffled_df = df.sample(frac=1).reset_index(drop=True)

# Save the shuffled data as a JSON file
json_file_path = 'shuffled_students.json'  # Replace with your desired output JSON file path
shuffled_df.to_json(json_file_path, orient='records')

# Deactivate the virtual environment (optional)
# Run this if you want to exit the virtual environment
# deactivate
