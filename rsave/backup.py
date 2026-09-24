from pathlib import Path
from datetime import datetime
import shutil

def backup(save_directory):
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    target_dir = Path("backup") / time_stamp
    target_dir_specific = target_dir / save_directory.name

    target_dir.mkdir(parents=True)

    if save_directory.is_dir():
        shutil.copytree(save_directory, target_dir_specific)
    elif save_directory.is_file():
        shutil.copy2(save_directory, target_dir)