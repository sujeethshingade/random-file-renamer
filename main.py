import os
import random
import shutil

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def shuffle_and_copy_rename_files(src_directory, renamed_directory):
    files = [file for file in os.listdir(src_directory) if os.path.isfile(os.path.join(src_directory, file))]

    if not files:
        print("No files found in the directory.")
        return

    random.shuffle(files)

    for index, file in enumerate(files):
        file_extension = os.path.splitext(file)[1]
        new_filename = f"file_{index + 1}{file_extension}"
        old_file_path = os.path.join(src_directory, file)
        new_file_path = os.path.join(renamed_directory, new_filename)

        try:
            shutil.copy(old_file_path, new_file_path)
            print(f"Copied and renamed: {file} -> {new_filename}")
        except Exception as e:
            print(f"Error renaming {file}: {e}")

    print(f"\nSuccessfully copied and renamed {len(files)} files!")

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))
    original_files_folder = os.path.join(base_directory, 'original_files')
    renamed_files_folder = os.path.join(base_directory, 'renamed_files')

    create_directory(renamed_files_folder)
    shuffle_and_copy_rename_files(original_files_folder, renamed_files_folder)