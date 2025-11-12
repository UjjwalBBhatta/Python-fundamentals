# src/folder_creator.py
from pathlib import Path
from . import logger, FILE_CATEGORIES

def create_folders(base_path):
    """
    Create folders based on FILE_CATEGORIES dictionary.
    Returns a mapping of extension -> folder path.
    """
    folder_map = {}
    base_path = Path(base_path)

    for category, extensions in FILE_CATEGORIES.items():
        folder_path = base_path / category
        try:
            folder_path.mkdir(exist_ok=True)
            logger.log(f"Folder ready: {folder_path}")
        except PermissionError:
            logger.log(f"⚠️ Permission denied: Cannot create folder {folder_path}")
            continue

        for ext in extensions:
            folder_map[ext.lower()] = folder_path

    return folder_map
