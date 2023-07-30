import os
from google_drive import get_drive_service
from dotenv import load_dotenv
from config.games_config import games_config
from sqlalchemy.orm import Session
from config.sqlachemy import SessionLocal
from models.console import Console

def insert_file_data(file_name: str, file_url: str, console_name: str):
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
    session = SessionLocal()

    for game_config in games_config:
        console = session.query(Console).filter_by(name=game_config['name']).first()
        print("console: ", console)
        response = drive_service.files().list(q=f"'{game_config['id']}' in parents",
                                              fields="files(id, name, webViewLink)").execute()
        files = response.get('files', [])
        for file in files:
            file_name = file.get('name', '')
            file_url = file.get('webViewLink', '')
            print(f"Found file: {file_name} ({file_url})")
            insert_file_data(file_name, file_url, game_config['name'])

    session.close()

if __name__ == "__main__":
    main()
