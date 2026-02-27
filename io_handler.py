
import os

def get_all_files(folder_path): # Scount and return all the file based on the config data_folder
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                all_files.append(os.path.join(root, file))
    return all_files

def read_file(file_path): #return in str
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def write_log(results, log_file="log.txt"): # using for log operations
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            for filename, count in results.items():
                f.write(f"{filename}: {count}\n")
    except Exception as e:
        print(f"Error writing log: {e}")
