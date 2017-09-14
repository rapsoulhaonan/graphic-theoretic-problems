import os
import sys

a = "hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar  -file mapper.py    -mapper \'mapper.py "

b = "\' -file reducer.py   -reducer reducer.py -input google_graph -output t1"
recursion = 0;
start_point = '0';             # start point
target_point = '38716';        # destination 
arg_list = '';
flag = True;

os.system("hadoop fs -rm -r t1")    
os.system("rm -r t1")

while flag:                 # while not reach destination
   if recursion == 0:         # first iteration use start point as arg
      os.system(a + str(start_point) + b)
   else:
      print a + str(arg_list) + b
      os.system(a + str(arg_list) + b)
      
   os.system("hadoop fs -copyToLocal t1 t1")
   f = open('t1/part-00000')       # fetch reducer output for next iteration
   arg_list = '';
   for line in f:
      line = line.strip()
      if str(line) == str(target_point):  # check for destination
         flag = False
      else:
         arg_list = str(arg_list) + " " + line
   
   recursion = recursion + 1         # recursion time is the distance

   if flag:
      os.system("hadoop fs -rm -r t1")
      os.system("rm -r t1")
   else:
      print recursion
   
