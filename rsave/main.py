from pathlib import Path


save_directory = (input("Enter save directory: "))

stripped_input = save_directory.strip('"')

stripped_path = Path

if stripped_path.is_dir():
    print("Directory. END")
    for file in stripped_path.iterdir():
        print(file.name)
elif stripped_path.is_file():
    print("File. END")
else:
    print("Does not exist or invalid input")