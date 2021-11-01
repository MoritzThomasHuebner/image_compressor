These are just some handy scripts that I use to sort and compress my photos. The compression is based on the `PIL` packages which needs to be installed separately.

###`compress_all_images.py`
This script takes four arguments `uncompressed_dir`, `compressed_dir`, `quality`, `overwrite`. 
All image files in `uncompressed_dir` will be compressed and outputted in `compressed_dir`, while preserving the subdirectory structure.
`quality` is an integer between 1 and 100 with 100 perfectly preserving the quality.
`overwrite` sets whether existing image files in `compressed_dir` will be overwritten.

###`delete_old_raws.py`
This script takes two arguments `dir`, and `number_of_days`.
All raw files within `dir` that are older than `number_of_days` will be deleted.

###`sort_files.py`
This script creates some useful subdirectories for all photos in `dir` by figuring out the date taken either from the image name or the image metadata.
The script may not work properly on differently formatted dates within image names.
The script then sorts the files into subdirectories like this: `dir/year/month`