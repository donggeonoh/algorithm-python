from sys import maxsize


def dijkstra(graph, start, end):
    shortest_distance = [maxsize for _ in range(graph.len)]
    visited = set()

    shortest_distance[start] = 0

    for _ in range(graph.len):
        min_vertex = min_distance_vertex(shortest_distance, visited)
        visited.add(min_vertex)

        for vertex, edge in enumerate(graph.edges(min_vertex)):
            if edge and shortest_distance[min_vertex] + edge < shortest_distance[vertex]:
                shortest_distance[vertex] = shortest_distance[min_vertex] + edge

    return None if shortest_distance[end] == maxsize else shortest_distance[end]


def min_distance_vertex(iter, visited):
    min_value = maxsize
    min_index = maxsize

    for index, value in enumerate(iter):
        if index not in visited and value < min_value:
            min_index = index

    return None if min_value == maxsize else min_index
