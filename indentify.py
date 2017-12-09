import re
import argparse
from autofocus import AFSample

#OWkey = <OverWatch API Key>
#AFkey = <AutoFocus API Key>

#Define all Arguments.
parser = argparse.ArgumentParser()
parser.add_argument("f", "--fileName", help="List to injest")
parser.add_argument("--OverWatchKey", help="Your API key for OverWatch")
parser.add_argument("--AutoFocusKey", help="Your API key for AutoFocus")
args = parser.parse_args()
inputFile = args.fileName

OWkey = args.OverWatchKey
AFkey = args.AutoFocusKey

#prep dicts for passing to indentify func
md5 = []
sha1 = []
sha256 = []
ip = []

def indentify(line, ip, md5, sha1, sha256):
    other = []

    if re.search(r"( (?:[0-9]{1,3}\.){3}[0-9]{1,3} ), line):
        ip.append(line)

    elif re.match(r"([A-Fa-f0-9]{64})", line):
        sha256.append(line)

    elif re.match(r"([a-fA-F\d]{40})", line):
        sha1.append(line)

    elif re.match(r"([a-fA-F\d]{32})", line):
        md5.append(line)

    else other.append(line)

def toSha256(md5, sha1):
    for sample in md5:
        try:
            sha256.append( AFSample.get(sample).sha256 )
        except error:
            print("This sample was not found in AutoFocus")
    for sample in sha1:
        try:
            sha256.append( AFSample.get(sample).sha256 )
        except error:
            print("This sample was not found in AutoFocus")

def main():
    with open( inputFile ,'r') as FileIn
        for line in FileIn:
            indentify(line, ip, md5, sha1, sha256)

    toSha256(md5, sha1)


if __name__ == "__main__":
    main()
