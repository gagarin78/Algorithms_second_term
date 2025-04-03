def bellman_ford(n, edges, start):
    distances = {node: float('inf') for node in range(1, n + 1)}
    distances[start] = 0
    
    for _ in range(n - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    negative_cycle = set()
    for _ in range(n):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = -float('inf')
                negative_cycle.add(v)

    result = []
    for i in range(1, n + 1):
        if distances[i] == float('inf'):
            result.append("*")
        elif i in negative_cycle:
            result.append("-")
        else:
            result.append(str(distances[i]))
    
    return result

def main():
    with open("input.txt", "r") as f:
        n, m, s = map(int, f.readline().split())
        edges = [tuple(map(int, line.split())) for line in f.readlines()]

    output = bellman_ford(n, edges, s)

    with open("output.txt", "w") as f:
        f.write("\n".join(output) + "\n")

if __name__ == '__main__':
    main()