#!/usr/bin/env python

import argparse
import datetime
import os
from pathlib import Path
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--dir", default="XT30", type=str)
args = parser.parse_args()

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for dirpath, _, filenames in os.walk(args.dir):
    for filename in filenames:
        if filename.startswith("201") or filename.startswith("202"):
            stripped_filename = filename.replace("-", "").replace(".", "").replace("_", "")
            year = stripped_filename[:4]
            month = stripped_filename[4:6]
            new_dir_path = os.path.join(args.dir,
                                        f"{year}/{month}_{MONTHS[int(month) - 1]}")
        else:
            creation_time = os.path.getmtime(os.path.join(dirpath, filename))
            date = datetime.datetime.fromtimestamp(creation_time)
            new_dir_path = os.path.join(args.dir,
                                        f"{date.year}/{str(date.month).zfill(2)}_{MONTHS[date.month - 1]}")

        Path(new_dir_path).mkdir(parents=True, exist_ok=True)
        old_path = os.path.join(dirpath, filename)
        new_path = os.path.join(new_dir_path, filename)
        os.rename(old_path, new_path)


