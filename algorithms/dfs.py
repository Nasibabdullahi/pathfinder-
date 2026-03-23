def dfs(grid, start, goal, visualize):
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        visualize.visit(node)

        if node == goal:
            return reconstruct_path(parent, start, goal)

        for neighbor in grid.get_neighbors(node):
            if neighbor not in visited:
                parent[neighbor] = node
                stack.append(neighbor)
                visualize.frontier(neighbor)

    return None


def reconstruct_path(parent, start, goal):
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()
    return path