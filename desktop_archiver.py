import os
import shutil
from datetime import datetime

# Path to Desktop
DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")

# Folder name like 'Archived_Desktop_2025-06-11'
date_str = datetime.now().strftime("%Y-%m-%d")
archive_folder_name = f"Archived_Desktop_{date_str}"
archive_folder_path = os.path.join(DESKTOP, archive_folder_name)

# Create archive folder if it doesn't exist
os.makedirs(archive_folder_path, exist_ok=True)

# Move everything except the archive folder itself
for item in os.listdir(DESKTOP):
    src_path = os.path.join(DESKTOP, item)
    dst_path = os.path.join(archive_folder_path, item)

    # Skip the archive folder itself (in case it's re-run)
    if src_path == archive_folder_path:
        continue

    try:
        shutil.move(src_path, dst_path)
        print(f"Moved: {item}")
    except Exception as e:
        print(f"Failed to move {item}: {e}")
