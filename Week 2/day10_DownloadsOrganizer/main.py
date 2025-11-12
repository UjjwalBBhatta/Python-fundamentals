from src.scanner import scan_folder
from src.folder_creator import create_folders
from src.file_mover import move_files
from src import logger
from pathlib import Path

def main():
    logger.log("🚀 Starting File Organizer...")

    folder_to_organize = "C:/Users/ujjwa/Downloads"

    files = scan_folder(folder_to_organize)  
    logger.log(f"Found {len(files)} files in current directory.")

    if not files:
        logger.log("No files found. Exiting.")
        return

    folder_map = create_folders(folder_to_organize)
    move_files(files, folder_map)

    logger.log("✅ All files organized successfully!")

if __name__ == "__main__":
    main()
