#!/usr/bin/env python

import sys
import re

def usage():
    print("Usage: " + sys.argv[0] + " FILE")

if len(sys.argv) == 1:
    print(sys.argv[0] + ": missing file name argument")
    usage()
    sys.exit(1)

if sys.argv[1] == '-h' or sys.argv[0] == '--help':
    usage()
    sys.exit(0)

argFile = sys.argv[1]

# Open file (read mode) and load lines in the fileContainer list
fileContainer = [] 

content = open(argFile, 'r')
while True:
    line = content.readline()
    if line != '':
        fileContainer.append(line)    
    else:
        break
content.close()

# Print cleaning up extra \n line endings
for item in fileContainer:
    print(re.sub('\\n', '', item))

sys.exit(0)
