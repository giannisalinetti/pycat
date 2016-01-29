#!/usr/bin/env python
"""This small utulity is a test program made during a train travel from Milan to Rome.
   Its purpose is to show file contents using lists to load lines.
"""

import sys
import re


def usage():
    """Prints program usage"""
    print("Usage: " + sys.argv[0] + " FILE")


def argsCheck():
    """Checks program arguments"""
    if len(sys.argv) == 1:
        print(sys.argv[0] + ": missing file name argument")
        usage()
        sys.exit(1)

    if sys.argv[1] == '-h' or sys.argv[0] == '--help':
        usage()


def listLoad(argFile):
    """Takes a file as an argument and returns a raw list of its lines"""    
    fileContainer = [] 
    content = open(argFile, 'r')
    while True:
        line = content.readline()
        if line != '':
            fileContainer.append(line)    
        else:
            break
    content.close()
    return fileContainer


def main():
    """Main function"""
    argsCheck()
    rawOutList = listLoad(sys.argv[1])

    # Print cleaning up extra \n line endings
    for item in rawOutList:
        print(re.sub('\\n', '', item))
    return(0)

if __name__ == '__main__':
    main()


