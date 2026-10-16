def dfs_tree(tree, root, goal, trace=None):
    stack = LifoQueue()
    stack.put([root])
    visited = []

    while not stack.empty():
        path = stack.get()
        node = path[-1]
        visited.append(node)

        if node == goal:
            record(trace, node, [p[-1] for p in stack.queue], visited)
            return path

        for child in reversed(tree[node]):
            stack.put(path + [child])

        record(trace, node, [p[-1] for p in stack.queue], visited)

    return None


def dfs_graph(graph, start, goal, trace=None):
    stack = [[start]]
    visited = []

    while stack:
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            record(trace, node, [p[-1] for p in stack], visited)
            return path

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(path + [neighbor])

        record(trace, node, [p[-1] for p in stack], visited)

    return None