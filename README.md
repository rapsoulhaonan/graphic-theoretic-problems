# graphic-theoretic-problems

Graphs are mathematical structures used to model pair-wise relations between objects from a certain collection. Graph can be defined a set V of vertices and set of edges. Where, V is collection of |V| = n abstract data types. These abstract data types are also called nodes. 

In computer science, graphs are used to represent networks of communication, data organization, computational devices, the flow of computation, etc. For instance, the link structure of a website can be represented by a directed graph, in which the vertices represent web pages and directed edges represent links from one page to another. 

MapReduce is a framework for processing parallelizable problems across huge datasets using a large number of computers (nodes), collectively referred to as a cluster or a grid. MapReduce is useful in a wide range of applications, including distributed pattern-based searching, distributed sorting, web link-graph reversal, Singular Value Decomposition, web access log stats, inverted index construction, document clustering, machine learning, and statistical machine translation.

Using mapreduce method to solve graph problem is a tempting idea. Because nowadays, data is increasing in size every day, traditional ways of data analysis will finally be out-of-date. Taking the advantage of parallel computing is an inevitable trend. In this project, we tried to solve several graph problems by writing a program using Hadoop streaming.

## problem 1

1)	Given a node N, find all nodes exactly K hops away. Put another way, starting at a domain, find all web pages one can reach in 3 clicks.

## problem 2

2)	For a given pair of nodes X and Y, find the shortest distance from X to Y where distance is defined as the number of links to get from X to Y in a directed graph.

## problem 3

3)	For a node X, find the transitive closure of X (that is, the set of all nodes reachable from X).

## setting 

This project used a 16-node graph we created to test and demonstrate programs and algorithm. A google web graph from Google programming contest was also used to test and analysis programs. Since this is just an elementary exploration, we used a relatively simple model, unweighted directed graph. The graph given as a table with two columns, the first column is the ID of the start node while the second column is the ID of the target point. For example:

#

![graph](image/1.PNG)

![graph](image/2.PNG)

## design

The idea behinds three problems is the same, that is: start from a given point search its neighbor nodes, goes one step further every time until reach the terminate condition. Iterations is the same for every problem: search target nodes of start points in the graph (a table of pairs of vertexes) and use IDs of target nodes as the start points of the next iteration.

##

For problem 1: assume we need to find nodes that are 2 hops away from 13. Perform iterations until iteration time is equal to the 2. After iterations, the current target points are the nodes that are k hops away from 13.

#

![graph](image/3.PNG)

##

For problem 2: assume we need to find the shortest distance from 13 to 2. Using 13 as the initial start point and perform iterations until node 2 is found as a target node. At this point, the iteration times is the distance from 13 to 2.

#

![graph](image/4.PNG)

##

For problem 3: assume we start from 13, and record the ID of node that has been visited. When there is no new ID being record, terminate the iteration. The nodes recorded at this point is the transitive closure of 13.

#

![graph](image/5.PNG)

![graph](image/6.PNG)

##

In a word, all these three problems could be solved using breadth-first search. The different between a normal BFS and a BFS with Map/Reduce is that in a normal BFS, the program goes through neighbor nodes one by one while Map/Reduce goes through every neighbor nodes in a single run. 

#

![graph](image/7.PNG)

## implementation

Several different implementations were tried, and the final practical design contains the following components:
-	Mapper: take one or more arguments as the ID of starting points, goes through the graph to find targets nodes of starting points. Once find a target nodes, map its ID.
-	Reducer: remove duplicated ID and output incoming IDs.
-	Driver: the driver program manages iterations. It extracts the result from reducer and feed the result to mapper as the arguments for the next iteration. When the terminate condition is fulfilled, the driver ends the program and output the result.

The processes are as follow:
-	First iteration:
   Driver calls mapper using a pre-defined node ID (the original start point) as an argument. Mapper sends IDs of target nodes of the original start point out. The reducer discard duplicated IDs and output the rest of them to a file (a bunch of IDs).

-	Iterations after the first one:
Driver fetch the content of output file from reducer and delete the file, then calls mapper using the content from output file as arguments (a bunch of IDs). Mapper takes arguments as start points, and map their target nodes. The reducer discard duplicated IDs and output the rest to a file (a bunch of IDs).
Repeat until the terminate condition is fulfilled.
