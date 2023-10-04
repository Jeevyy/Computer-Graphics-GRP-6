import os
import zipfile
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

"""Paths to your local files"""
File_paths = [
    'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/translations.json',
    'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/JSONL_Output',
    'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/Excel_Files'
]

"""Path to your Google API credentials JSON file"""
translations_file_path = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/translations.json'
jsonl_output_dir = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/JSONL_Output'
excel_files_dir = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/Excel_Files'


"""This is the Path to the Google API credentials JSON file in the local computer"""
credentials_file_path = 'C:/Users/User/Downloads/group-5-400916-b4f38ed28334.json'

"""Load the Google API credentials"""
credentials = service_account.Credentials.from_service_account_file(
    credentials_file_path, scopes=['https://www.googleapis.com/auth/drive']
)

"""Build the Google Drive API service"""
"""The below code builds the Google Drive API service"""

credentials_file_path = 'C:/Users/User/Downloads/group-5-400916-b4f38ed28334.json'


credentials = service_account.Credentials.from_service_account_file(credentials_file_path,
                                                                    scopes=['https://www.googleapis.com/auth/drive'])

drive_service = build('drive', 'v3', credentials=credentials)


def get_folder_id_by_name(folder_name):
    # Search for the folder by name
    results = drive_service.files().list(
        q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'").execute()
    items = results.get('files', [])

    if items:
        return items[0]['id']
    else:
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')


def create_zip_file(file_paths, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            zipf.write(file_path, arcname=file_name)
"""Get the ID of the "group6" folder or create it if it doesn't exist"""

group6_folder_id = get_folder_id_by_name("group6")


def upload_to_drive(local_file_path, drive_folder_id=None):
    # Define the file metadata
    file_metadata = {
        'name': os.path.basename(local_file_path),  # Name of the file on Google Drive
    }

    if drive_folder_id:
        file_metadata['parents'] = [drive_folder_id]

    media = MediaFileUpload(local_file_path)
    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    file_id = uploaded_file.get('id')
    return file_id


# temporary zip folder
zip_folder_name = 'temp.zip'
create_zip_file(File_paths, zip_folder_name)
"""translations.json file to the "group6" folder"""


"""translations.json file to "group6" folder"""
translations_file_id = upload_to_drive(translations_file_path, group6_folder_id)

# Get the drive folder
group6_folder_id = get_folder_id_by_name("group6")

# Upload the zipped folder to Google Drive
zip_file_id = upload_to_drive(zip_folder_name, group6_folder_id)


os.remove(zip_folder_name)

print(f"Files zipped and uploaded to Google Drive successfully as '{zip_folder_name}'")