import os, sys, getopt, base64
import xml.etree.ElementTree as ET

def resx2files(resx, outdir):
    tree = ET.parse(resx)
    root = tree.getroot()

    os.makedirs(outdir, exist_ok=True)

    for data in root.iter('data'):
        name = data.get('name')
        type = data.get('type')
        value = data.findtext('value')
        filename = os.path.join(outdir, name)
        if isinstance(type, str) and type.startswith('System.Byte[]'):
            bin = base64.decodebytes(bytes(value, 'ASCII'))
            with open(filename, 'bw') as f:
                f.write(bin)
        else:
            with open(filename, 'w') as f:
                f.write(value)


def usage():
    print(f'usage: python3 {sys.argv[0]} [--help] [-o OUTDIR] FILE\n')
    print(f'optional arguments:')
    print(f'  -h, --help    show this help message and exit')
    print(f'  -o OUTDIR     use OUTDIR as output directory, default: the input filename without extension')
    print(f'  FILE          The input filename')
    print()
    print(f'example:')
    print(f'  python3 {sys.argv[0]} Device.resx')


try:
    optlist, args = getopt.getopt(sys.argv[1:], 'ho:', ['help'])
except getopt.error as err:
    print(err)
    usage()
    sys.exit(2)

if len(optlist) == 0 and len(args) == 0 or len(args) > 1:
    usage()
    sys.exit(0)

file = args[0]
outdir = os.path.splitext(os.path.basename(file))[0]

for current_argument, current_value in optlist:
    if current_argument in ('-h', '--help'):
        usage()
        sys.exit(0)
    elif current_argument in ('-o'):
        outdir = current_value

resx2files(file, outdir)
