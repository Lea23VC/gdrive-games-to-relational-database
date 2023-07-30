import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
import json

load_dotenv()  # take environment variables from .env

# Parse the JSON data from the environment variable
google_auth_data = os.getenv('GOOGLE_AUTH')

def get_drive_service():
    if google_auth_data:
        SCOPES = ['https://www.googleapis.com/auth/drive']
        SERVICE_ACCOUNT_FILE = json.loads(google_auth_data)  # Replace with the path to your Service Account key JSON file

        print(SERVICE_ACCOUNT_FILE)
        credentials = service_account.Credentials.from_service_account_info(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        return build('drive', 'v3', credentials=credentials)
    
    else:
        raise ValueError("GOOGLE_AUTH environment variable is not set.")
