from _collections import defaultdict


class Graph:
    def __init__(self):
        # self.list = []
        self.graph = defaultdict(list) # nush man literally asa am gasit pe net ma fut in el

    def add_edge(self, node, edge):
        self.graph[node].append(edge)

    def bfs_method(self, start_node):
        visited = [False] * (len(self.graph))  # inca nu am vizitat niciun nod
        queue = [start_node]  # am nodul de start
        visited[start_node] = True  # il vizitez
        while queue:  # cat timp mai am elemente in lista
            start_node = queue.pop(0)  # elimin nodul vizitat
            print(start_node, end=" ")  # il afisez
            for current_node in self.graph[start_node]:  # ma uit in vecinii sai
                if not visited[current_node]:  # daca nu e vizitat
                    queue.append(current_node)  # il adaug in lista de vizitari
                    visited[current_node] = True  # este vizitat
