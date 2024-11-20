import os
import sys

def rename_files_sequentially(directory):
    try:
        files = os.listdir(directory)
        for i, filename in enumerate(files):
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, f"file{i+1}{os.path.splitext(filename)[1]}")
            os.rename(old_file, new_file)
        print("Files renamed successfully.")
    except FileNotFoundError:
        print("Directory not found:", directory)
    except PermissionError:
        print("Permission denied for accessing:", directory)
    except OSError as e:
        print("Error renaming files:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
    else:
        rename_files_sequentially(sys.argv[1])
