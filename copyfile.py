import os
import shutil
import argparse
parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
parser.add_argument('-s','--source', help='source file absolute path',required=True)
parser.add_argument('-d','--destination',help='destination absolute path', required=True)
args = parser.parse_args()
try:
	shutil.copy(args.source, args.destination)
        print "file copied successfully"
except Exception as e:
	print e
