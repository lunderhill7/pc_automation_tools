import os
import time
import shutil
from datetime import datetime

# -------- CONFIG --------
DAYS_OLD = 30
# ------------------------

# Ask user for folder to cleanblade putter
input_path = input("Enter the full path to the folder you want to clean: ").strip() 

# Verify it exists
if not os.path.isdir(input_path):
    print("That folder does not exist.")
    exit()

# Calculate cutoff time
now = time.time()
cutoff = now - (DAYS_OLD * 86400)

# Create archive folder
date_str = datetime.now().strftime("%Y-%m-%d")
archive_folder = os.path.join(input_path, f"OldFiles_{date_str}")
os.makedirs(archive_folder, exist_ok=True)

moved_count = 0

for filename in os.listdir(input_path):
    filepath = os.path.join(input_path, filename)

    if os.path.isfile(filepath):
        file_modified = os.path.getmtime(filepath)

        if file_modified < cutoff:
            try:
                shutil.move(filepath, os.path.join(archive_folder, filename))
                print(f"Moved: {filename}")
                moved_count += 1
            except Exception as e:
                print(f"Failed to move {filename}: {e}")

print(f"\nFinished. {moved_count} file(s) moved to {archive_folder}")
