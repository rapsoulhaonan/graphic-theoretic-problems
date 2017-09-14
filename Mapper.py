#!/usr/bin/env python

import sys
import os

num_nodes = len(sys.argv)

for line in sys.stdin:            # go through graph
   line = line.strip()
   words = line.split()
   origin = long(words[0])
   target = long(words[1])
   
   for i in range(1,num_nodes):  # find neighbors of given node
      if long(sys.argv[i]) == origin:
         print '%d' % (target)       # map neighbor nodes
