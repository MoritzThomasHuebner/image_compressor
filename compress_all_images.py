#!/usr/bin/env python

import argparse
import os
from pathlib import Path

from PIL import Image


def compress(image_label, uncompressed_image_path, compressed_image_path, quality=80, overwrite=False):
    if not overwrite:
        if os.path.isfile(os.path.join(compressed_image_path, image_label)):
            return
    with Image.open(os.path.join(uncompressed_image_path, image_label)) as im:
        exif = im.info['exif']
        im.save(os.path.join(compressed_image_path, image_label), quality=quality, optimize=True, exif=exif)


parser = argparse.ArgumentParser()
parser.add_argument("--uncompressed_dir", default="XT30", type=str)
parser.add_argument("--compressed_dir", default="XT30_compressed", type=str)
parser.add_argument("--quality", default=80, type=int)
parser.add_argument("--overwrite", default="False", type=str)
args = parser.parse_args()

overwrite = args.overwrite == "True"


for dirpath, _, filenames in os.walk(args.uncompressed_dir):
    new_dir_path = args.compressed_dir + dirpath.lstrip(args.uncompressed_dir)
    Path(new_dir_path).mkdir(parents=True, exist_ok=True)
    for filename in filenames:
        if filename[-4:].lower() == ".jpg" or filename[-5:].lower() == ".jpeg":
            compress(image_label=filename, uncompressed_image_path=dirpath,
                     compressed_image_path=new_dir_path, quality=args.quality, overwrite=overwrite)
