#!/usr/bin/env python

from operator import itemgetter
import sys

current_node = None

for line in sys.stdin:
    line = line.strip()
    if line:
       if current_node:             # discard duplicated node
          if current_node != line:
             current_node = line
             print '%s' % (line)
       else:
          current_node = line
          print '%s' % (line)            # output to file
