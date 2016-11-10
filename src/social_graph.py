import csv
import sys


class Node(object):
    """ 
    Node class representing each user 
    """
    def __init__(self, name, degree):
        self._degree = degree
        self._name = name
        self._visited = False
        self._neighbor_list = []


    def add_neighbor(self, node_id):
        if not node_id in self._neighbor_list:
            self._neighbor_list.append(node_id)


    def set_degree(self, degree):
        self._degree = degree


    def set_visited(self, visited):
        self._visited = visited


class Graph(object):
    """ 
    Graph data structure representing soical network graph of users
    """
    def __init__(self):
        self._graph = {}
        self._visited_nodes = set() 

   
    def add(self, node_id1, node_id2):
        """ Add connection between node1 and node2 """
        
        if not node_id1 in self._graph:
            node1 = Node(node_id1, 0)
            self._graph[node_id1] = node1
        self._graph[node_id1].add_neighbor(node_id2)

        if not node_id2 in self._graph:
            node2 = Node(node_id2, 0)
            self._graph[node_id2] = node2
        self._graph[node_id2].add_neighbor(node_id1)


    def reset(self):
        """ reset the visited nodes in the graph """

        for node in self._visited_nodes:
            self._graph[node].set_degree(0)
            self._graph[node].set_visited(False)


    def bfs_search(self, node_id1, node_id2, max_degree):
        """ search if node_id2 is within max_degree of node_id1 """

        try:
            node1 = self._graph[node_id1]
            node2 = self._graph[node_id2]
        except KeyError:
            return False

        queue = [node_id1]
        self._visited_nodes.add(node_id1)

        while len(queue):
            node_id = queue.pop(0)
            node = self._graph[node_id]
            node._visited = True

            if node._degree > max_degree:
                return False
            
            if node._name == node_id2:
                return True

            for neighbor_node_id in node._neighbor_list:
                neighbor_node = self._graph[neighbor_node_id]

                if not neighbor_node._visited:
                    neighbor_node.set_degree(node._degree+1)
                    neighbor_node._visited = True
                    queue.append(neighbor_node_id)
                    self._visited_nodes.add(neighbor_node_id)        
        return False


