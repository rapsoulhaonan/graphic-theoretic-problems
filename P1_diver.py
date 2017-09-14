import os
import sys

a = "hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar  -file mapper.py    -mapper \'mapper.py "

b = "\' -file reducer.py   -reducer reducer.py -input g -output t1"

recursion = 3;                   # how many hops from the start point
start_point = '13';                # start point
arg_list = '';

os.system("hadoop fs -rm -r t1")    # remove folder for next iteration
os.system("rm -r t1")

for i in range(0,recursion):         
   if i == 0:                    # First iteration: use start_point as arg
      os.system(a + str(start_point) + b)   
   else:
      print a + str(arg_list) + b       
      os.system(a + str(arg_list) + b)  
      

   os.system("hadoop fs -copyToLocal t1 t1")  # fetch output of reducer
   f = open('t1/part-00000')      
   arg_list = '';
   for line in f:
      line = line.strip()
      arg_list = str(arg_list) + " " + line      # save reducer output for
                                       # next iteration
 
   if i != recursion - 1:                    # if not finished, remove 
      os.system("hadoop fs -rm -r t1")       # intermediate folder
      os.system("rm -r t1")

   else:
      print arg_list                      # print final result
