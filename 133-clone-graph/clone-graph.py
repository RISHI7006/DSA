"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Maps original node -> cloned node
        visited = {}
        
        def dfs(original):
            # If we've already cloned this node, return the clone (avoids infinite loop)
            if original in visited:
                return visited[original]
            
            # Create clone and register it BEFORE recursing into neighbors
            clone = Node(original.val)
            visited[original] = clone
            
            # Recursively clone all neighbors and attach them
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)