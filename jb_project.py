# coding=utf-8

from collections import deque


class Graph:
    """Klasa dla grafu ważonego, skierowanego lub nieskierowanego."""

    def __init__(self, n, directed=False):
        self.n = n  # kompatybilność
        self.directed = directed  # bool, czy graf skierowany
        self.matrix = []  # macierz sasiedztwa
        self.matrix = []  # macierz sasiedztwa
        for x in range(n):
            self.matrix.append([0 for x in range(n)])

        self.clear_values()

    def v(self):  # zwraca liczbę wierzchołków
        return self.n

    def e(self):  # zwraca liczbę krawędzi
        edges_count = 0
        for row in self.matrix:
            for x in row:
                if x is not 0:
                    edges_count += 1
        return edges_count

    def is_directed(self):  # bool, czy graf skierowany
        return self.directed

    def add_edge(self, e_from, e_to, e_weight=1):  # wstawienie krawędzi
        if self.has_edge(e_from, e_to) is False:
            self.matrix[e_from][e_to] = e_weight
            if self.directed is False:
                self.matrix[e_to][e_from] = e_weight
        else:
            print("Podana krawedz juz istnieje")

    def has_edge(self, e_from, e_to):  # bool
        return self.matrix[e_from][e_to] != 0

    def weight(self, e_from, e_to):  # zwraca wagę krawędzi
        return self.matrix[e_from][e_to]

    def iter_adjacent(self, node):  # iterator po wierzchołkach sąsiednich
        for i in range(0, self.n):
            if self.matrix[node][i] != 0:
                yield i

    def print_graph(self):  # drukuje graf w postaci macierzy sasiedztwa
        print("       Macierz sasiedztwa")
        s = "   "
        for x in range(self.n):
            s += str(x)
            s += "  "
        print(s)
        for x in range(self.n):
            print(x, self.matrix[x])

    def clear_values(self):  # resetuje wartosci tablic
        self.time = 0  # tablica przechowujaca o ilosci przetwarzania wierzcholkow
        self.color = ["white"] * self.n  # tablica przechowujaca kolory wierzcholkow
        self.start = [0] * self.n  # tablica przechowujaca informacje o starcie przetwarzania wierzcholkow
        self.end = [0] * self.n  # tablica przechowujaca informacje o zakonczeniu przetwarzania wierzcholkow
        self.parent = [None] * self.n  # tablica przechowujaca informacje o rodzicach wierzcholkow
        self.distance = [float(
            "inf")] * self.n  # tablica przechowujaca informacje o odleglosci od wierzcholka startowego

    def bfs(self, start):
        self.clear_values()
        q = deque()
        self.color[start] = "grey"
        self.distance[start] = 0
        self.parent[start] = None

        q.appendleft(start)
        while len(q) > 0:
            u = q.pop()
            for i in self.iter_adjacent(u):
                if self.color[i] is "white":
                    self.color[i] = "grey"
                    self.distance[i] = self.distance[u] + 1
                    self.parent[i] = u
                    q.appendleft(i)
            self.color[u] = "black"

    def dfs(self):
        self.clear_values()
        for u in range(0, self.n):
            if self.color[u] is "white":
                self.visit_node(u)

    def visit_node(self, u):
        self.color[u] = "grey"
        self.time += 1
        self.start[u] = self.time
        for i in self.iter_adjacent(u):
            if self.color[i] is "white":
                self.parent[i] = u
                self.visit_node(i)
        self.color[u] = "black"
        self.time += 1
        self.end[u] = self.time
