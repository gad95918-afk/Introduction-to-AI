def bfs_tree(tree, root, goal, trace=None):
    queue = deque()
    queue.append([root])
    visited = []

    while queue:
        path = queue.popleft()
        node = path[-1]
        visited.append(node)

        if node == goal:
            record(trace, node, [p[-1] for p in queue], visited)
            return path

        for child in tree[node]:
            queue.append(path + [child])

        record(trace, node, [p[-1] for p in queue], visited)

    return None


def bfs_graph(graph, start, goal, trace=None):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            record(trace, node, [p[-1] for p in queue], visited)
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])

        record(trace, node, [p[-1] for p in queue], visited)

    return None