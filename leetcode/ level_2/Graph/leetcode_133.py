"""Clone Graph"""
"""Link to the problem: https://leetcode.com/problems/clone-graph/"""
import networkx as nx
import matplotlib.pyplot as plt


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

    def buildGraph(self, adj_list):
        if not adj_list:
            return None

        # Create a list to hold all the nodes, indexed by their value - 1 (for 1-based indexing)
        nodes = [Node(i + 1) for i in range(len(adj_list))]

        # Build the graph
        for i, neighbors in enumerate(adj_list):
            for n in neighbors:
                # Adjust index by -1, since the nodes are 1-indexed in the problem description
                nodes[i].neighbors.append(nodes[n - 1])

        # Return the head node of the graph
        return nodes[0]

    def drawGraph(self, node):
        if not node:
            return None
        queue = [node]
        visited = set()

        graph = nx.DiGraph()

        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            for neighbor in current.neighbors:
                graph.add_edge(current.val, neighbor.val)
                graph.add_edge(neighbor.val, current.val)
                queue.append(neighbor)
        # Draw the graph
        pos = nx.spring_layout(graph)  # positions for all nodes
        nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'), node_size=500)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), arrows=True)
        plt.title("Graph Visualization")
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    solution = Solution()
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

    # Build graph from adjacency list
    node = solution.buildGraph(adjList)
    # Draw the graph
    solution.drawGraph(node)

    copy_node = solution.cloneGraph(node)
    solution.drawGraph(copy_node)
