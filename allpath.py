class Solution:
    def __init__(self):
        self.list_of_path = []
        self.path = []

    def allPathsSourceTarget(self, graph):
        """
            >>> a = Solution()
            >>> Solution.allPathsSourceTarget(a, [[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
            True
            >>> b = Solution()
            >>> Solution.allPathsSourceTarget(b, [[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
            True
        """
        visited = [False for elem in graph]
        self.from_and_to(graph, 0, len(graph) - 1, visited, self.path)
        return self.list_of_path

    def from_and_to(self, graph, fromm, to, visited, path):
        visited[fromm] = True
        self.path.append(fromm)
        if fromm == to:
            self.list_of_path.append(self.path.copy())
        else:
            for vertex in graph[fromm]:
                if visited[vertex] == False:
                    self.from_and_to(graph, vertex, to, visited, path)
        self.path.pop()
        visited[fromm] = False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
