import sys

sys.setrecursionlimit(10**6)

def read_input(filename):
    with open(filename, "r") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
    return n, graph

def dfs(v, graph, color):
    color[v] = 1
    for neighbor in graph[v]:
        if color[neighbor] == 1:
            return True
        if color[neighbor] == 0 and dfs(neighbor, graph, color):
            return True
    color[v] = 2
    return False

def has_cycle(n, graph):
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            if dfs(i, graph, color):
                return True
    return False

def main():
    input_file = "input.txt"
    output_file = "output.txt"

    n, graph = read_input(input_file)

    result = "1\n" if has_cycle(n, graph) else "0\n"

    with open(output_file, "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
