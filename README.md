
##Challenge Summary

This project implements three features of a "digital wallet", which aims to prevent fraudulent payment requests from untrusted users. 

Developed by Yan Jiang, Nov, 2016, Python 3. 
 
####Feature 1
When a payment happens between people who are not a 1st degree connection, a warning should be sent, and the output file 1 should have "unverified". 

####Feature 2
When a payment happens between people who are not a 2nd degree connection, a warning should be sent, and the output file 2 should have "unverified". 

####Feature 3
When a payment happens between people who are not a 4th degree connection, a warning should be sent, and the output file 3 should have "unverified". 

####Feature (optional)
When a payment happens between people who are not a nth degree connection, a warning should be sent, and the output file n should have "unverified". 

##Data Structure

[Back to Table of Contents] (README.md#table-of-contents)

The social network is represented as a undirected graph, with each user id defined as a node.This problem can be viewed as searching the distance between two nodes in an undirected graph. This is the best fit for BFS, while DFS tends to become complex and rise potential errors. 


###Select data structure for graph: 
The graph should support two functions: 1) search nodes; 2) modify (insert). Therefore, a hash table is a best candidate for this job. The time complexity of doing search, insert, are both O(1). The space complexity is {V + E}.  

A library social_graph was developed to define two classes: 	

###Graph class:represent user network using a hash table
Each user id as key and each node (Node type) as value, with the following methods defined: 

add(self, node_id1, node_id2)                    # check if node exsit and add to graph

reset(self)                                       # only reset the nodes that have been visited, not the whole graph. 

bfs_search(self, node_id1, node_id2, max_degree)  # search two nodes within the max_degree in the graph

###Node class: represent each individual user
the following attributes defined:  

self._name = name          # user id

self._degree = degree      # degree of potential friend,

self._visited = False      # whether node has been visited

self._neighbor_list = []   # all its neighbors' id


##Search the Social Network Graph
The search of n-th degree friend was implemented by a Breadth-first search (BFS). 

####Why not Depth-first search (DFS)? 

DFS and BFS are two commonly used algrithm to search through graph. DFS is often more effcient than BFS in terms of time complexcity. However, in case, since the soical network is a undirected graph, which frequently contains cycles. Cycle would make it difficult to determine the right degree of connection, since it is possible to visit the node from both directions.  Therefore, BFS is the best to implement this search task. 

####BFS time complexity analysis: 
The worst case is visiting all n-degree nodes and edges, which is {V+E}, where V, E are vertex and edges insides the n-degree network. 

###How the algrithm is the optimized for computation efficiency
####1. Use appropriate data structure coupled with search algrithm

Since the social network can grow very large, to make sure it is efficient to search a node, a hash table is the best choice, since the average time complexcity of a search is O(1). Search the graph is implemented by queue. The average time complexcity of insertion and deletion in queue is O(1). 

####2. Save time by only reset visited nodes
Reset the nodes on the whole graph can consume lots of time. Record the visited nodes and only reset that part could improve the efficiency. 
 

##Additional features could help detect fraud

In the future, the degree of friend can be set to detect a n-th degree connection network, this would be helpful if interested in examining connections with higher degrees. 

To implement any n-degree connection warning, call the function bfs_search(self, node_id1, node_id2, max_degree) and set the max_degree to n. 



##How to run or test the program
####command line for csv input files: 

python antifraud.py batch_payment.csv stream_payment.csv output1.txt output2.txt output3.txt

or for txt input files:

python antifraud.py batch_payment.txt stream_payment.txt output1.txt output2.txt output3.txt

####Or use shell script (default is txt input file format):

./run.sh

####To run the tests:  
./run_tests.sh

##Repo directory structure
[Back to Table of Contents] (README.md#table-of-contents)

Submission Repo Structure

	├── README.md 
	├── run.sh
	├── src
	│  	└── antifraud.py
	|       └── social_graph.py (library)  
	|
	└── insight_testsuite
	 	   ├── run_tests.sh
		   └── tests
	        	└── test-1-paymo-trans
        		│   ├── paymo_input
        		│   │   └── batch_payment.csv
        		│   │   └── stream_payment.csv
        		│   └── paymo_output
        		│       └── output1.txt
        		│       └── output2.txt
        		│       └── output3.txt
        		└── yan-test-1
            		├── paymo_input
        		│     │   └── batch_payment.csv
        		│     │   └── stream_payment.csv
        		│     │  
        		│     └── paymo_output
        		│         └── output1.txt
        		│         └── output2.txt
        		│         └── output3.txt
			|-- yan-test-2
            		├── paymo_input
        		│    │   └── batch_payment.txt
        		│    │   └── stream_payment.txt
        		│    └── paymo_output
        		│        └── output1.txt
        		│        └── output2.txt
        		│        └── output3.txt
		        └── yan-test-3
            		     ├── paymo_input
        		     │   └── batch_payment.csv
        		     │   └── stream_payment.csv
        		     └── paymo_output
        		         └── output1.txt
        		         └── output2.txt
        		         └── output3.txt

