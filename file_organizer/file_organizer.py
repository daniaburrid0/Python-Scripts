"""
Python script to organize files in a folder by their type. Create folders with the name of the extension for each type and move the files to their corresponding folder.
"""
import os
import shutil

def main():
    # Get user input for the folder path
    folder_path = input("Enter the path of the folder you want to organize: ")

    # Check if the path exists
    if not os.path.exists(folder_path):
        print("The provided folder path does not exist.")
        return

    # Organize the files
    organize_files(folder_path)

def organize_files(folder_path):
    # Get a list of all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the item is a file and not a system file
        if os.path.isfile(file_path) and not filename.startswith("."):
            file_ext = os.path.splitext(filename)[1]

            # Create a new folder for the file extension if it doesn't exist
            new_folder_path = os.path.join(folder_path, file_ext)

            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            # Move the file into the corresponding folder
            shutil.move(file_path, os.path.join(new_folder_path, filename))

if __name__ == "__main__":
    main()
