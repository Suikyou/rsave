from pathlib import Path
from datetime import datetime
import shutil

def backup(save_directory):
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    target_dir = Path("backup") / time_stamp
    target_dir_specific = target_dir / save_directory.name

    try:
        target_dir.mkdir(parents=True)

        if save_directory.is_dir():
            shutil.copytree(save_directory, target_dir_specific)
        elif save_directory.is_file():
            shutil.copy2(save_directory, target_dir)
    except OSError as error:
        if target_dir.exists():
            shutil.rmtree(target_dir)
        print("Backup failed.")
        print(error)
    else:
        print(f"Backup successful. Location is at {target_dir}")