# generateDataset.py

import os
import random
import sys

def generate_dataset(num_files, data_folder="data"):
    os.makedirs(data_folder, exist_ok=True)
    keywords = ["error", "warning", "failed", "success"]
    normal_text = "This is a sample log line."
200
    for i in range(1, num_files + 1):
        filename = f"{data_folder}/file_{i}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            num_lines = random.randint(5000,10000)
            for _ in range(num_lines):
                line = f"{normal_text} {random.choice(keywords) if random.random() < 0.2 else ''}\n"
                f.write(line)
    print(f"Generated {num_files} files in '{data_folder}' folder.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generateDataset.py <number_of_files>")
        sys.exit(1)

    try:
        num_files = int(sys.argv[1])
        generate_dataset(num_files)
    except ValueError:
        print("Please provide a valid integer for number of files.")
        sys.exit(1)
