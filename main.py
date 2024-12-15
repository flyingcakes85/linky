import argparse
import os


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


    print("hello world")
    