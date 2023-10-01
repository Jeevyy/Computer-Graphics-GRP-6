import os

from functions import copy_jsonl_files, create_excel_files, process_excel_files, generate_translations_json


def main():
    """
    1.Update the project directory,
    2.Import extracted JSONL files
    3.Generate Excel files from JSONL files,
    4.Generate test, train, and dev JSONL files for select languages
    5.Generate a translations.json file
    """

    project_dir = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6'

    source_dir = 'C:/Users/User/Desktop/New folder'
    destination_dir = os.path.join(project_dir, 'JSONL_Files')
    os.makedirs(destination_dir, exist_ok=True)
    copy_jsonl_files(source_dir, destination_dir)

    jsonl_dir = os.path.join(project_dir, 'JSONL_Files')
    output_dir = os.path.join(project_dir, 'Excel_Files')
    os.makedirs(output_dir, exist_ok=True)
    create_excel_files(jsonl_dir, output_dir)

    excel_dir = output_dir
    jsonl_output_dir = os.path.join(project_dir, 'JSONL_Output')
    os.makedirs(jsonl_output_dir, exist_ok=True)
    process_excel_files(excel_dir, jsonl_output_dir)

    generate_translations_json(jsonl_output_dir, os.path.join(project_dir, 'translations.json'))


if __name__ == "__main__":
    main()
