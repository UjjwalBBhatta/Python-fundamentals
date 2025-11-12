
from pathlib import Path

def scan_folder(folder_path=None):
    """Scan the folder and return a list of file paths."""
    if folder_path is None:
        folder_path = Path.cwd()
    else:
        folder_path = Path(folder_path)
    
    files = [f for f in folder_path.iterdir() if f.is_file()]
    return files

    