# 🧰 PC Automation Toolkit

A suite of Python scripts designed to automate everyday desktop file maintenance tasks, including organizing downloads, cleaning old files, archiving the desktop, and detecting duplicate files.

---

## 📦 Contents

### 1. `downloads_organizer.py`

Sorts files in your Downloads folder into categorized subfolders (Images, Documents, Archives, etc.).

* **Skills shown:** file handling, sorting logic, automation
* **Usage:** Automatically organizes Downloads based on file extensions

### 2. `desktop_archiver.py`

Moves everything on your Desktop into a dated archive folder (e.g., `Archived_Desktop_2025-06-11`).

* **Skills shown:** working with dates, file/folder manipulation
* **Usage:** Reduces desktop clutter with one click

### 3. `old_file_cleaner.py`

Finds files older than a specified number of days in a chosen folder and moves them into an archive folder.

* **Features:**

  * User-input folder path
  * Non-destructive (moves files, doesn't delete)
* **Skills shown:** time comparisons, user input, dynamic path handling

### 4. `duplicate_finder.py`

Scans a folder for true duplicate files (based on SHA-256 hash) and optionally moves duplicates to the Recycle Bin.

* **Features:**

  * Byte-for-byte comparison using hashing
  * Skips large files by default (>100MB)
  * Safe deletion using `send2trash`
* **Skills shown:** hashing, chunked file reading, safe file deletion

### 5. `main.py`

Launcher script providing a CLI menu to run all tools from one place.

---

## 🚀 How to Use

1. Clone/download the repository or copy the files into a folder
2. Open a terminal inside the project directory
3. Run:

   ```bash
   python main.py
   ```
4. Follow the on-screen menu to select a tool

---

## 🛠 Dependencies

* Python 3.6+
* `send2trash` for safe Recycle Bin support (used in `duplicate_finder.py`):

  ```bash
  pip install send2trash
  ```

---

## 📌 Notes

* All tools are safe by design — no destructive actions without explicit confirmation
* File paths and folder names are either dynamically detected or requested from the user
* Designed to run locally on Windows (but compatible with macOS/Linux with small tweaks)

---

## 📄 License

MIT License (or modify this section based on your intended license)

---

## ✍️ Author

Luke Underhill 
Personal Automation Project - 2025
