import unittest

from jb_project import Graph


class Tests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(8, True)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(2, 5)
        self.graph.add_edge(2, 6)
        self.graph.add_edge(4, 7)

        self.graphUndir = Graph(7)
        self.graphUndir.add_edge(0, 1)
        self.graphUndir.add_edge(0, 2)
        self.graphUndir.add_edge(0, 3)
        self.graphUndir.add_edge(1, 3)
        self.graphUndir.add_edge(2, 3)
        self.graphUndir.add_edge(2, 4)
        self.graphUndir.add_edge(3, 5)
        self.graphUndir.add_edge(4, 6)

    def test_bfs(self):
        self.graph.bfs(0)
        self.assertEqual(self.graph.distance, [0, 1, 1, 2, 2, 2, 2, 3])
        self.assertEqual(self.graph.parent, [None, 0, 0, 1, 1, 2, 2, 4])

        self.graphUndir.bfs(0)
        self.assertEqual(self.graphUndir.distance, [0, 1, 1, 1, 2, 2, 3])
        self.assertEqual(self.graphUndir.parent, [None, 0, 0, 0, 2, 3, 4])

    def test_dfs(self):
        self.graph.dfs()
        self.assertEqual(self.graph.start, [1, 2, 10, 3, 5, 11, 13, 6])
        self.assertEqual(self.graph.end, [16, 9, 15, 4, 8, 12, 14, 7])

        self.graphUndir.dfs()
        self.assertEqual(self.graphUndir.start, [1, 2, 4, 3, 5, 10, 6])
        self.assertEqual(self.graphUndir.end, [14, 13, 9, 12, 8, 11, 7])

    def test_edges_count(self):
        self.assertEqual(self.graph.e(), 7)
        self.assertEqual(self.graphUndir.e(), 16)

    def test_vertices_count(self):
        self.assertEqual(self.graph.v(), 8)
        self.assertEqual(self.graphUndir.v(), 7)

    def test_print(self):
        self.graph.print_graph()
        print
        self.graphUndir.print_graph()


if __name__ == '__main__':
    unittest.main()
