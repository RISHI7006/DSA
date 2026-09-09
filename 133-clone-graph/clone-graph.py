class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Attach the cloned neighbor to the cloned current node
                visited[current].neighbors.append(visited[neighbor])
        
        return visited[node]