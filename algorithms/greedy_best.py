import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first(grid, start, goal, visualize):
    pq = []
    heapq.heappush(pq, (0, start))

    visited = set()
    parent = {}

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        visualize.visit(node)

        if node == goal:
            return reconstruct_path(parent, start, goal)

        for neighbor in grid.get_neighbors(node):
            if neighbor not in visited:
                priority = heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))
                parent[neighbor] = node
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