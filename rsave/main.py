from pathlib import Path
from backup import backup

#variables
save_directory = Path(input("Enter save directory: ").strip('"'))

#logic
if not save_directory.is_dir() and not save_directory.is_file():
    print("Does not exist or invalid input.")
    exit()

backup(save_directory)