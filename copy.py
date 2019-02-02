#!/usr/bin/python 

import sys

try:
  src = sys.argv[1]
  dest = sys.argv[2]
except Exception as e:
    print "pls pass the src and dest"

import commands
s, o = commands.getstatusoutput('cp %s %s' %(src, dest))


sys.exit()

