from pathlib import Path
import os

# Show all files and folders
def read_files_and_folders():
    path = Path()
    items = list(path.rglob('*'))

    print("\nAvailable Files & Folders:\n")
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


# Create File
def create_file():
    try:
        read_files_and_folders()

        name = input("\nEnter file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as f:
                data = input("Enter content: ")
                f.write(data)

            print("✅ File created successfully")
        else:
            print("⚠️ File already exists")

    except Exception as err:
        print(f"❌ Error: {err}")


# Read File
def read_file():
    try:
        read_files_and_folders()

        name = input("\nEnter file name to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, "r") as f:
                print("\n📄 File Content:\n")
                print(f.read())

            print("\n✅ File read successfully")
        else:
            print("⚠️ File does not exist")

    except Exception as err:
        print(f"❌ Error: {err}")


# Update File
def update_file():
    try:
        read_files_and_folders()

        name = input("\nEnter file name to update: ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("\n1. Rename file")
            print("2. Overwrite file")
            print("3. Append data")

            choice = int(input("Enter your choice: "))

            # Rename
            if choice == 1:
                new_name = input("Enter new file name: ")
                p.rename(new_name)
                print("✅ File renamed successfully")

            # Overwrite
            elif choice == 2:
                with open(p, "w") as f:
                    data = input("Enter new content: ")
                    f.write(data)
                print("✅ File overwritten successfully")

            # Append
            elif choice == 3:
                with open(p, "a") as f:
                    data = input("Enter content to append: ")
                    f.write(" " + data)
                print("✅ Data appended successfully")

            else:
                print("⚠️ Invalid choice")

        else:
            print("⚠️ File does not exist")

    except Exception as err:
        print(f"❌ Error: {err}")


# Delete File
def delete_file():
    try:
        read_files_and_folders()

        name = input("\nEnter file name to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
            print("✅ File deleted successfully")
        else:
            print("⚠️ File does not exist")

    except Exception as err:
        print(f"❌ Error: {err}")


# Main Menu
def main():
    while True:
        print("\n===== Python File Manager =====")
        print("1. Create File")
        print("2. Read File")
        print("3. Update File")
        print("4. Delete File")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_file()
            elif choice == 2:
                read_file()
            elif choice == 3:
                update_file()
            elif choice == 4:
                delete_file()
            elif choice == 5:
                print("👋 Exiting program...")
                break
            else:
                print("⚠️ Invalid choice")

        except ValueError:
            print("⚠️ Please enter a valid number")


if __name__ == "__main__":
    main()
