import os
import sys

a = "hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar  -file mapper.py    -mapper \'mapper.py "

b = "\' -file reducer.py   -reducer reducer.py -input g -output t1"

recursion = 0;
start_point = '13';                # start point
arg_list = '';
graph_nodes = [];                # record visited nodes
graph_nodes.append(start_point);   # add start point to visited record
flag = True;

os.system("hadoop fs -rm -r t1")    # clear for reducer output
os.system("rm -r t1")

while flag:
   if recursion == 0:
      os.system(a + str(start_point) + b)
   else:
      print a + str(arg_list) + b
      os.system(a + str(arg_list) + b)
      
   recursion = recursion + 1

   os.system("hadoop fs -copyToLocal t1 t1")
   f = open('t1/part-00000')
   arg_list = '';
   len_before = len(graph_nodes)   
   for line in f:
      line = line.strip()
      arg_list = str(arg_list) + " " + line
      exist = False;
      for j in graph_nodes:
         if line == j:
            exist = True
      if not exist:
         graph_nodes.append(line)   # if node not recorded, then record
   len_after = len(graph_nodes)
   if len_after == len_before:  # if no new record incoming, terminate 
      flag = False
 
   if flag:
      os.system("hadoop fs -rm -r t1")
      os.system("rm -r t1")
   else:
      print graph_nodes
