import os
import shutil

# Get path to your Downloads folder
DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

# File types grouped by category
DESTINATIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
    "Executables": [".exe", ".msi"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
    "Music": [".mp3", ".wav", ".flac"],
}

def organize_downloads():
    for filename in os.listdir(DOWNLOADS):
        filepath = os.path.join(DOWNLOADS, filename)

        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            moved = False

            for folder, extensions in DESTINATIONS.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(DOWNLOADS, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(filepath, os.path.join(target_folder, filename))
                    print(f"Moved: {filename} -> {folder}/")
                    moved = True
                    break

            if not moved:
                print(f"Skipped (unrecognized type): {filename}")

if __name__ == "__main__":
    organize_downloads()
