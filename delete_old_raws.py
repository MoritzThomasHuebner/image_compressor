#!/usr/bin/env python

import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("--dir", default="XT30", type=str)
parser.add_argument("--number_of_days", default=30, type=int)
args = parser.parse_args()


for dirpath, _, filenames in os.walk(args.dir):
    for filename in filenames:
        if filename[-4:].lower() == ".raf":
            creation_time = os.path.getmtime(os.path.join(dirpath, filename))
            current_time = time.time()
            days_since_photo_taken = (current_time-creation_time)/86400
            if days_since_photo_taken > args.number_of_days:
                os.remove(os.path.join(dirpath, filename))

