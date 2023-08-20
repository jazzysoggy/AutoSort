from pathlib import Path
import fnmatch
import os
import shutil

# Get the user's home directory
home = Path.home()

# Special folder names

document = {
    ".pdf",
    ".doc",
    ".xls",
    ".xlsx",
    ".txt",
    ".log",
    ".csv",
    ".docx"
}

photos = {
    ".jpg",
    ".jpeg",
    ".png",
    ".heic"
}

videos = {
    ".mp4",
    ".mkv",
    ".wmv",
    ".mov"
}

music = {
    ".mp3",
    ".m4a",
    ".wav",
    ".aac",
    ".wma",
    ".flac"
}

archival = {
    ".zip",
    ".exe",
    ".msi",
}

programming = {
    ".rbxl",
    ".rbxm",
    ".cpp",
    ".hpp",
    ".h",
    ".py"
}

downloads = Path(home / "Downloads")
if downloads.exists():
    directory_path = Path(home / "Downloads")
    files = [f for f in directory_path.iterdir() if f.is_file()]
    for file in files:
        file_extension = os.path.splitext(file)[1]
        path_to_move_from = home / "Downloads" / file.name
        path_to_move_to = home / "Downloads" / file.name
        if file_extension in document and Path(home / "Documents").exists():
            path_to_move_to = home / "Documents" / file.name
        elif file_extension in music and Path(home / "Music").exists():
            path_to_move_to = home / "Music" / file.name
        elif file_extension in videos and Path(home / "Videos").exists():
            path_to_move_to = home / "Videos" / file.name
        elif file_extension in photos and Path(home / "Pictures").exists():
            path_to_move_to = home / "Pictures" / file.name
        elif file_extension in archival and Path(home / "Documents").exists():
            if not Path(home / "Documents" / "Archive").exists():
                Path(home / "Documents" / "Archive").mkdir(parents=True, exist_ok = True)
            path_to_move_to = home / "Documents" / "Archive" / file.name
        elif file_extension in programming and Path(home / "Documents").exists():
            if not Path(home / "Documents" / "Programming").exists():
                Path(home / "Documents" / "Programming").mkdir(parents=True, exist_ok = True)
            path_to_move_to = home / "Documents" / "Programming" / file.name
        else:
            print("Can't Find Location")

        if not path_to_move_to.exists():
            shutil.move(file, path_to_move_to)
            print(f"Moved {file.name} to {path_to_move_to}")
        else:
            print(f"File {file.name} already exists in the destination.")

