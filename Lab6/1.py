import os
import sys

def read_and_print_files(directory, extension):
    try:
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        if not files:
            print("No files found with extension", extension)
            return
        
        for filename in files:
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as file:
                    print(file.read())
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    except FileNotFoundError:
        print("The directory does not exist:", directory)
    except PermissionError:
        print("Permission denied for accessing:", directory)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <extension>")
    else:
        read_and_print_files(sys.argv[1], sys.argv[2])
