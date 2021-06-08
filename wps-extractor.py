#!/usr/bin/env python3
import os
import json
import argparse


def extract(var):
    if hasattr(var,'items'):
        name = None
        source = None
        for k, v in var.items():
            if k == 'name':
                name = v
            if k == 'source':
                source = v
            if name and source:
                yield name, source
            if isinstance(v, dict):
                for result in extract(v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in extract(d):
                        yield result


def process_file(bundle_file:str, name:str, source:str, dir:str = None):
    if not dir:
        print(f"##### {bundle_file} {name} #####\n\n")
        print(source)
        print("\n\n")    
    else:
        file_path = dir.rstrip(r'\/') + os.path.sep + bundle_file + os.path.sep + name.lstrip(r'.\/')
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(file_path, 'w') as f:
            print(f'{file_path}')
            f.write(source)


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Extract modules source code from Angular (WebPack bundle statistics) stats.json files (https://webpack.js.org/api/stats/)')
    parser.add_argument('file', nargs='+', help='webpack stats json file(s)')
    parser.add_argument('-d', type=str, help='If set, store files to this directory (with dir structure) else all sources go to stdout')

    args = parser.parse_args()

    if args.d:
        if not os.path.exists(args.d):
            print (f"Directory {args.d} not exists!")
            return

    for bundle_file in args.file:
        stats_obj = None
        with open(bundle_file , "r") as f:
            stats_obj = json.load(f)

        for n, s in extract(stats_obj):
            process_file(bundle_file, n, s, args.d)

if __name__ == "__main__":
    main()
