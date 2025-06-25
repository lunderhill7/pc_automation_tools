import os
import hashlib
from send2trash import send2trash

# -------- Settings --------
MAX_FILE_SIZE_MB = 100  # Skip files larger than this
# --------------------------

# Ask user for folder to scan
input_path = input("Enter the full path to the folder you want to scan for duplicates: ").strip()

# Verify it exists
if not os.path.isdir(input_path):
    print("That folder does not exist.")
    exit()

# Function to calculate SHA256 hash of a file
def get_file_hash(filepath):
    hasher = hashlib.sha256()
    try:
        print(f"Scanning: {filepath}")
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"⚠️ Skipping {filepath} (error reading file): {e}")
        return None

# Map from hash to list of files with that content
hashes = {}

# Walk through all files in the directory
for root, _, files in os.walk(input_path):
    for name in files:
        filepath = os.path.join(root, name)

        try:
            if os.path.getsize(filepath) > MAX_FILE_SIZE_MB * 1024 * 1024:
                print(f"Skipping large file: {filepath}")
                continue
        except Exception as e:
            print(f"⚠️ Skipping {filepath} (error checking size): {e}")
            continue

        file_hash = get_file_hash(filepath)

        if file_hash:
            hashes.setdefault(file_hash, []).append(filepath)

# Print out duplicates
duplicates = []
print("\n📂 Duplicate files found:\n")
for file_list in hashes.values():
    if len(file_list) > 1:
        print("----")
        for f in file_list:
            print(f)
        duplicates.append(file_list)

if not duplicates:
    print("✅ No duplicate files found.")
    exit()

# Ask user if they want to delete duplicates
answer = input("\nWould you like to move all duplicates (keeping one per group) to the Recycle Bin? (y/n): ").strip().lower()

if answer == 'y':
    trashed_count = 0
    for file_group in duplicates:
        for dup in file_group[1:]:  # Keep first file, remove the rest
            try:
                send2trash(dup)
                print(f"Moved to Recycle Bin: {dup}")
                trashed_count += 1
            except Exception as e:
                print(f"Failed to move {dup}: {e}")
    print(f"\n✅ Done. Moved {trashed_count} duplicate file(s) to Recycle Bin.")
else:
    print("❌ No files were moved.")
