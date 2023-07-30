from config.google_drive import get_drive_service
from config.games_config import games_config
from sqlalchemy.orm import Session
from config.sqlachemy import SessionLocal
from models.console import Console
from models.game import Game
from sqlalchemy.exc import IntegrityError
import os

def insert_file_data(file_name: str, file_url: str, console: Console, session: Session):
    try:
          # Remove the file extension from the file name
        game_name = os.path.splitext(file_name)[0]
        print(f"Inserting file '{game_name}'...")
        file = Game(name=game_name, url=file_url, console_id=console.id)
        session.add(file)
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
        page_token = None
        while True:
            query_params = {'q': f"'{game_config['id']}' in parents",
                            'fields': "files(id, name, webViewLink), nextPageToken",
                            'pageSize': 500}
            if page_token:
                query_params['pageToken'] = page_token

            response = drive_service.files().list(**query_params).execute()
            files = response.get('files', [])
            for file in files:
                file_name = file.get('name', '')
                file_url = file.get('webViewLink', '')
                print(f"Found file: {file_name} ({file_url})")
                insert_file_data(file_name, file_url, console, session)
            print("Committing changes...")
            session.commit()
            page_token = response.get('nextPageToken')
            if not page_token:
                break

            
    session.close()

if __name__ == "__main__":
    main()
