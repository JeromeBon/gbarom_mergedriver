#!/bin/env python
"""gbamerge
This is a custom merge driver for git. It should be called from git
with a stanza in .git/config like this:
    [merge "gbamerge"]
        name = A custom merge driver for roms
        driver = pathtothisfile %O %A %B %L
        recursive = binary
To make git use the custom merge driver you also need to put this in
.git/info/attributes (or in .gitattributes):
   *.gba merge=gbamerge
This tells git to use the 'gbamerge' merge driver to merge files called *.gba.
"""
import sys


def print_range(start, end, sep='  |  '):
    if start == end:
        print(hex(start), end=sep)
    else:
        print(hex(start) + '-' + hex(end), end=sep)


with open(sys.argv[1], 'rb') as f:
    ANCESTOR = f.read()
with open(sys.argv[2], 'rb') as f:
    CURRENT = f.read()
    current = bytearray(CURRENT)
with open(sys.argv[3], 'rb') as f:
    OTHER = f.read()

if not len(OTHER) == len(ANCESTOR) == len(current):
    sys.exit(1)

diffs = []
for i in range(len(current)):
    if  OTHER[i] != ANCESTOR[i]:
        if current[i] != ANCESTOR[i]:
            diffs.append(i)
        else:
            current[i] = OTHER[i]
if diffs:
    print("Can't resolve the conflict.", "Conflicting offsets are:")
    start = diffs[0]
    current = start
    for offset in diffs[1:]:
        if offset == current+1:
            current = offset
        else:
            print_range(start, current)
            start = offset
            current = offset
    print_range(start, current, sep='\n')
    sys.exit(1)

f = open(sys.argv[2],'wb')
f.write(current)
f.close()
sys.exit(0)
