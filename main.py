from config.google_drive import get_drive_service
from config.games_config import games_config
from sqlalchemy.orm import Session
from config.sqlachemy import SessionLocal
from models.console import Console
from models.game import Game
from sqlalchemy.exc import IntegrityError

def insert_file_data(file_name: str, file_url: str, console: Console, session: Session):
    try:
        # Check if the file with the same name already exists for the console
        existing_file = session.query(Game).filter_by(name=file_name, console_id=console.id).first()
        if existing_file:
            print(f"File '{file_name}' already exists for console '{console.name}'. Skipping...")
            return

        # Add the file to the database
        print(f"Inserting file '{file_name}'...")
        file = Game(name=file_name, url=file_url, console_id=console.id)
        session.add(file)
        session.commit()
    except IntegrityError as e:
        # Handle any integrity error (e.g., duplicate key) that might occur during commit
        session.rollback()
        print(f"Error inserting file '{file_name}': {str(e)}")
    except Exception as e:
        # Handle any other exceptions
        session.rollback()
        print(f"Error inserting file '{file_name}': {str(e)}")


def main():
    drive_service = get_drive_service()
    session = SessionLocal()

    for game_config in games_config:
        console = session.query(Console).filter_by(name=game_config['name']).first()
        response = drive_service.files().list(q=f"'{game_config['id']}' in parents",
                                              fields="files(id, name, webViewLink)",
                                              pageSize=200).execute()
        files = response.get('files', [])
        for file in files:
            file_name = file.get('name', '')
            file_url = file.get('webViewLink', '')
            print(f"Found file: {file_name} ({file_url})")
            insert_file_data(file_name, file_url, console, session)

    session.close()

if __name__ == "__main__":
    main()

