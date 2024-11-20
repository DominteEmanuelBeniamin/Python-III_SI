import os
import sys

def count_files_by_extension(directory):
    extension_count = {}
    try:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                ext = os.path.splitext(file)[1]
                if ext in extension_count:
                    extension_count[ext] += 1
                else:
                    extension_count[ext] = 1
        
        for ext, count in extension_count.items():
            print(f"{ext}: {count}")
    except FileNotFoundError:
        print("Directory not found:", directory)
    except PermissionError:
        print("Permission denied for accessing:", directory)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
    else:
        count_files_by_extension(sys.argv[1])
