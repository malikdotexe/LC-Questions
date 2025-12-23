"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #We could not directly use a visited set because 
        oldToNew = {}
        def clone(node):
            # If node is already cloned, return its copy
            if node in oldToNew:
                return oldToNew[node]
            #creating the copy node 
            copy = Node(node.val)
            #Assigning copy node to original node
            oldToNew[node] = copy
            for neig in node.neighbors:
                oldToNew[node].neighbors.append(clone(neig))

            #return cloned node
            return copy
        return clone(node) if node else None

#A boolean visited array only tells whether a node was seen, but it does not store the address of the cloned node.

# While cloning a graph, the same node can be reached again through a different path, and we must reuse the already created clone instead of creating a new one.

# To correctly connect edges, we need direct access to the cloned node, which is not possible with just a boolean.