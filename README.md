# resx2files
resx file extractor

The inverse of the Resgen.exe .NET tool. It handles text and binary resources.

```
usage: python3 resx2files.py [--help] [-o OUTDIR] FILE

optional arguments:
  -h, --help    show this help message and exit
  -o OUTDIR     use OUTDIR as output directory, default: the input filename without extension
  FILE          The input filename

example:
  python3 resx2files.py Device.resx
```
