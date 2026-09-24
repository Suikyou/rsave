from pathlib import Path


save_directory = Path(input("Enter save directory: ").strip('"'))

if save_directory.is_dir():
    print("Directory. END")
    for file in save_directory.iterdir():
        print(file.name)
elif save_directory.is_file():
    print("File. END")
else:
    print("Does not exist or invalid input")