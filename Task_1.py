import os
import shutil
import sys

def copy_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:] 
            if extension == "":
                extension = "no_extension"
            ext_dir = os.path.join(destination, extension)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            dest_file_path = os.path.join(ext_dir, file)
            try:
                shutil.copy2(file_path, dest_file_path)
            except Exception as e:
                print(f"Не вдалося скопіювати файл {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до вихідної директорії")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = "dist" if len(sys.argv) < 3 else sys.argv[2]

    copy_files(source_directory, destination_directory)

# командний рядок python Task_1.py /path/to/source /path/to/destination