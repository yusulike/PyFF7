#!/usr/bin/env python3
'''
Convert a TEX file to a regular image file
Niema Moshiri 2019
'''
from PyFF7.tex import TEX
from sys import argv,stderr
USAGE = "USAGE: %s <input_tex_file> <output_image_file>" % argv[0]

if __name__ == "__main__":
    if len(argv) != 3:
        print(USAGE); exit(1)
    img = TEX(argv[1]).get_pillow_image()
    img.save(argv[2])