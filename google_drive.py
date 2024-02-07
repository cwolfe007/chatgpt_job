import os.path
import io
import logging

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/documents"
]


def upload_to_drive(file_name, file_path):
    google_drive_folder_id = os.environ["GOOGLE_DRIVE_FOLDER_ID"]

    try:
        # create drive api client
        service = get_drive_service()
        file_metadata = {
            "name": file_name,
            "parents": [google_drive_folder_id],  # test folder
            "mimeType": "application/vnd.google-apps.document",
        }
        media = MediaFileUpload(file_path, mimetype="text/plain", resumable=True)
        # pylint: disable=maybe-no-member
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        print(f'File with ID: "{file.get("id")}" has been uploaded.')

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return file.get("id")


def get_file(real_file_id, file_type="txt"):
    try:
        # create drive api client
        service = get_drive_service()

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        if file_type == "txt":
            request = service.files().export_media(
                fileId=file_id, mimeType="text/plain"
            )
        else:
            request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            logging.debug(f"Download {int(status.progress() * 100)}.")
        # print(file.getvalue())
    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return file.getvalue()


def get_creds():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def get_drive_service():
    creds = get_creds()
    return build("drive", "v3", credentials=creds)
