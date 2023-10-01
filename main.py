import os

from functions import copy_jsonl_files, create_excel_files, process_excel_files, generate_translations_json


def main():
    # Update the project directory
    project_dir = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6'

    # Step 1: Copy JSONL files from source to destination directory
    source_dir = 'C:/Users/User/Desktop/New folder'
    destination_dir = os.path.join(project_dir, 'JSONL_Files')
    os.makedirs(destination_dir, exist_ok=True)
    copy_jsonl_files(source_dir, destination_dir)

    # Step 2: Generate Excel files from JSONL files
    jsonl_dir = os.path.join(project_dir, 'JSONL_Files')
    output_dir = os.path.join(project_dir, 'Excel_Files')
    os.makedirs(output_dir, exist_ok=True)
    create_excel_files(jsonl_dir, output_dir)

    # Step 3: Generate test, train, and dev JSONL files for select languages
    excel_dir = output_dir
    jsonl_output_dir = os.path.join(project_dir, 'JSONL_Output')
    os.makedirs(jsonl_output_dir, exist_ok=True)
    process_excel_files(excel_dir, jsonl_output_dir)

    # Step 4: Generate a translations.json file
    generate_translations_json(jsonl_output_dir, os.path.join(project_dir, 'translations/translations.json'))


if __name__ == "__main__":
    main()
