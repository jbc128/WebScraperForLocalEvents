import os
import shutil

def organize_downloads_folder(downloads_path):
    # Define file type folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
        'Programs': ['.exe', '.msi', '.apk', '.bat', '.sh'],
        'Others': []
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(downloads_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to corresponding folders
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)
        if os.path.isfile(file_path):
            moved = False
            ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if ext in extensions:
                    shutil.move(file_path, os.path.join(downloads_path, folder, filename))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(downloads_path, 'Others', filename))

# Example usage:
organize_downloads_folder(r'C:\Users\jarro\Downloads')