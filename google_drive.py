import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account


translations_file_path = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/translations.json'
jsonl_output_dir = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/JSONL_Output'
excel_files_dir = 'C:/Users/User/PycharmProjects/Computer-Graphics-GRP-6/Excel_Files'
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


"""translations.json file to "group6" folder"""
translations_file_id = upload_to_drive(translations_file_path, group6_folder_id)

"""files in the JSONL_Output directory """
for filename in os.listdir(jsonl_output_dir):
    if filename.endswith('.jsonl'):
        jsonl_file_path = os.path.join(jsonl_output_dir, filename)
        upload_to_drive(jsonl_file_path, group6_folder_id)

""" Excel_Files directory """
for filename in os.listdir(excel_files_dir):
    if filename.endswith('.xlsx'):
        excel_file_path = os.path.join(excel_files_dir, filename)
        upload_to_drive(excel_file_path, group6_folder_id)

print("Files uploaded to the 'group6' folder in Google Drive successfully.")