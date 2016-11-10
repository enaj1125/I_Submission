
##Challenge Summary

This project implements three features of a "digital wallet", which aims to prevent fraudulent payment requests from untrusted users. 
 
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

The social network is represented as a undirected graph, with each user id defined as a node. This makes a perfect application of an object-oriented programming design. In python, two classes were defined: 

###Node class: represent each individual user, with the following attributes defined:  

self._name = name          # user id

self._degree = degree      # degree of potential friend,

self._visited = False      # whether node has been visited

self._neighbor_list = []   # all its neighbors' id
	

###Graph class:represent user network using a hash table, with each user id as key and each node (Node type) as value.   

with the following methods defined: 

add(self, node_id1, node_id2)    

reset(self)

bfs_search(self, node_id1, node_id2, max_degree)



##Search the Social Network Graph
The search of n-th degree friend was implemented by a Breadth-first search (BFS). 

####Why not Depth-first search (DFS)? 

DFS and BFS are two commonly used algrithm to search through graph. DFS is often more effcient than BFS in terms of time complexcity. However, in case, since the soical network is a undirected graph, which possibly contains cycles. Therefore, BFS is the best to implement this search task. 

##Computation Efficiency and Optimization

###How the data structure best work for this case?
Since the social network can grow very large, to make sure it is efficient to search a node, a hash table is the best choice, since the average time complexcity of a search is O(1). 

Search the graph is implemented by queue, for which the average time complexcity of insertion and deletion is O(1).

###How the algrithm best optimized? 



####How do I test the performance?
It would be useful to know the performance of each functions, therefore, time library was used to measure the timing:

Functions that have been tested for time efficiency: 

bfs_search:  is a core function to determine the degree of friendship network. For the two 200MB+ input data, the average time for each bfs_search function call for 1000 computations is 0.0018s.  // nth degree

reading the input batch_payment and stream_payment csv files: take time xx s. // how long does it take to build the graph? 

reset function: reset the attributes of the visited nodes in the graph:  take time x s.  



##Additional features could help detect fraud
1) The degree of friend can be set to detect a n-th degree connection network, this would be helpful if interested in examining connections with higher degrees. 

2)

##How to run the program
####command line for csv input files: 

python antifraud.py batch_payment.csv stream_payment.csv output1.txt output2.txt output3.txt

or for txt input files:

python antifraud.py batch_payment.txt stream_payment.txt output1.txt output2.txt output3.txt

####Or use shell script (default is txt input file format):

./run.sh


##Repo directory structure
[Back to Table of Contents] (README.md#table-of-contents)

Submission Repo Structure

	├── README.md 
	├── run.sh
	├── src
	│  	└── antifraud.py
	├── paymo_input (conceptually included)
	│   └── batch_payment.csv
	|   └── stream_payment.csv
	├── paymo_output
	│   └── output1.txt
	|   └── output2.txt
	|   └── output3.txt
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
        		└── yan-test
            		 ├── paymo_input
        		     │   └── batch_payment.csv
        		     │   └── stream_payment.csv
        		     └── paymo_output
        		         └── output1.txt
        		         └── output2.txt
        		         └── output3.txt

