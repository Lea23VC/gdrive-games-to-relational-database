import os
from google_drive import get_drive_service
from dotenv import load_dotenv

# Load the environment variables from .env
load_dotenv()

# Define a list to store the folder IDs
FOLDER_IDS = [
    os.getenv('ID_FOLDER_GBA'),
    os.getenv('ID_FOLDER_GBC'),
    os.getenv('ID_FOLDER_GB'),
    os.getenv('ID_FOLDER_NES'),
    os.getenv('ID_FOLDER_SNES'),
    os.getenv('ID_FOLDER_64'),
    os.getenv('ID_FOLDER_GAMECUBE'),
    os.getenv('ID_FOLDER_DS'),
    os.getenv('ID_FOLDER_PSX'),
    os.getenv('ID_FOLDER_PS2'),
    os.getenv('ID_FOLDER_PSP'),
    os.getenv('ID_FOLDER_3DS'),
    os.getenv('ID_FOLDER_DREAMCAST'),
    os.getenv('ID_FOLDER_WII'),
    os.getenv('ID_FOLDER_SWITCH'),
    os.getenv('ID_FOLDER_GENESIS'),
]

# Print the list of folder IDs
print(FOLDER_IDS)
FOREIGN_KEY_VALUE = 1  # Replace with the foreign key value to link with another table in your database

def insert_file_data(file_name, file_url, foreign_key):
    # Implement your database insertion logic here
    # For example, you can use an ORM like SQLAlchemy or directly use SQL queries

    # Example using SQLAlchemy
    # Assuming you have a File model and a database session
    # from your SQLAlchemy setup
    # file = File(name=file_name, url=file_url, foreign_key=foreign_key)
    # session.add(file)
    # session.commit()
    pass

def main():
    drive_service = get_drive_service()

    for folder_id in FOLDER_IDS:
        response = drive_service.files().list(q=f"'{folder_id}' in parents",
                                              fields="files(id, name, webViewLink)").execute()
        files = response.get('files', [])
        for file in files:
            file_name = file.get('name', '')
            file_url = file.get('webViewLink', '')
            print(f"Found file: {file_name} ({file_url})")
            insert_file_data(file_name, file_url, FOREIGN_KEY_VALUE)

if __name__ == "__main__":
    main()
