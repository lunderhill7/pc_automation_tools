import os

def run_script(script_name):
    try:
        os.system(f"python {script_name}")
    except Exception as e:
        print(f"Error running {script_name}: {e}")

def main():
    while True:
        print("\n=== PC Automation Toolkit ===")
        print("1. Organize Downloads Folder")
        print("2. Archive Desktop")
        print("3. Clean Old Files (by date)")
        print("4. Find Duplicate Files")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            run_script("downloads_organizer.py")
        elif choice == '2':
            run_script("desktop_archiver.py")
        elif choice == '3':
            run_script("old_file_cleaner.py")
        elif choice == '4':
            run_script("duplicate_finder.py")
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
