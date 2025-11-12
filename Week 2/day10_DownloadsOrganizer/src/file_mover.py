import shutil
from pathlib import Path
from . import logger

def move_files(files, folder_map):
    """
    Move each file into the correct folder.
    Handles duplicate names and logs all actions.
    """
    for file in files:
        ext = file.suffix.lower()
        dest_folder = folder_map.get(ext)

        if not dest_folder:
            logger.log(f"Skipped: {file.name} (no matching folder)")
            continue

        dest_folder = Path(dest_folder)
        destination = dest_folder / file.name

        # Handle duplicate file names
        counter = 1
        original_name = file.stem
        while destination.exists():
            destination = dest_folder / f"{original_name} ({counter}){file.suffix}"
            counter += 1

        # Move the file
        try:
            shutil.move(str(file), str(destination))
            logger.log(f"Moved: {file.name} → {dest_folder}")
        except PermissionError:
            logger.log(f"⚠️ Permission denied: Cannot move {file.name}")
        except Exception as e:
            logger.log(f"⚠️ Error moving {file.name}: {e}")
