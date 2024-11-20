import os
import sys

def calculate_total_size(directory):
    total_size = 0
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                total_size += os.path.getsize(filepath)
        print("Total size:", total_size, "bytes")
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
        calculate_total_size(sys.argv[1])
