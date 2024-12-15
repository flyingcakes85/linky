import argparse
import os
import json
from pathlib import Path

def build(links, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
    except:
        print("Couldn't create build directory at " + output_dir)
    
    for i in links:
        output_file = Path(output_dir + "/" + i + "/index.html")
        output_file.parent.mkdir(exist_ok=True, parents=True)
        output_file.write_text(f"<!doctype html><meta http-equiv=\"refresh\" content=\"0; url={links[i]}\" />")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Linky',
                    description='Generate static site of short links',
                    epilog='created by Snehit Sah')
    parser.add_argument('links')
    parser.add_argument('-o', '--output-dir', default="build")

    args = parser.parse_args()

    with open(args.links) as f:
        links = json.load(f)

    build(links, args.output_dir)
