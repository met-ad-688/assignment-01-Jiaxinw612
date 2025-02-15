import os

file_path = "README.md"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        word_count = len(content.split())
        print(f"Word count in {file_path}: {word_count}")
else:
    print(f"{file_path} not found.")
