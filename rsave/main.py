from pathlib import Path
from datetime import datetime

#variables
save_directory = Path(input("Enter save directory: ").strip('"'))
time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
target_dir = Path("backup") / time_stamp

#logic
if save_directory.is_dir():
    for file in save_directory.iterdir():
        print(file.name)
    print("Directory backup successful", time_stamp)
elif save_directory.is_file():
    print("File backup successful", time_stamp)
else:
    print("Does not exist or invalid input")
    exit()

target_dir.mkdir(parents=True, exist_ok=True)