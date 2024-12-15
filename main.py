import argparse
import os
import json
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Linky',
                    description='Generate static site of short links',
                    epilog='created by Snehit Sah')
    parser.add_argument('links')
    parser.add_argument('-o', '--output-dir', default="build")

    args = parser.parse_args()
    print(args.links, args.output_dir)

    try:
        os.makedirs(args.output_dir, exist_ok=True)
    except:
        print("Couldn't create build directory at " + args.output_dir)

    with open(args.links) as f:
        d = json.load(f)
    
    for i in d:
        print(i + d[i])
        output_file = Path(args.output_dir + "/" + i + "/index.html")
        output_file.parent.mkdir(exist_ok=True, parents=True)
        print(output_file)
        output_file.write_text(f"<!doctype html><meta http-equiv=\"refresh\" content=\"0; url={d[i]}\" />")

    
    print("hello world")
    