# Webpack Stats Extractor
Extract modules source code from Angular (WebPack bundle statistics) stats.json files

## Basic usage
dump the source files keeping the directory structure in the specified path (must exist):
```
python3 wps-extractor.py stats.json -d out_directory/
```
dump all sources to one file:
```
python3 wps-extractor.py stats.json > sources.txt
```

## Options
```
usage: wps-extractor.py [-h] [-d D] file [file ...]

Extract modules source code from Angular (WebPack bundle statistics) stats.json files (https://webpack.js.org/api/stats/)

positional arguments:
  file        webpack stats json file(s)

optional arguments:
  -h, --help  show this help message and exit
  -d D        If set, store files to this directory (with dir structure) else all sources go to stdout (default: None)
```
