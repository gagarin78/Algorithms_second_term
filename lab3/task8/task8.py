import heapq
import time
import tracemalloc

def main():
    tracemalloc.start()
    start_time = time.time()

    with open('lab3/task8/input.txt', 'r') as f:
        data = f.readlines()
    
    n, m = map(int, data[0].split())
    
    graph = [[] for _ in range(n+1)]
    for line in data[1:m+1]:
        u, v, w = map(int, line.split())
        graph[u].append((v, w))
    
    start, end = map(int, data[m+1].split())
    
    INF = float('inf')
    distances = [INF] * (n + 1)
    distances[start] = 0
    heap = [(0, start)]
    
    # Основной цикл алгоритма
    while heap:
        current_dist, current_vertex = heapq.heappop(heap)
        
        if current_vertex == end:
            break
        
        if current_dist > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    with open('lab3/task8/output.txt', 'w') as f:
        if distances[end] != INF:
            f.write(f"{distances[end]}\n")
        else:
            f.write("-1\n")
    
    end_time = time.time()
    print(f"Time: {end_time - start_time:.4f}s")
    current, peak = tracemalloc.get_traced_memory()
    print(f"Memory: {peak / 1024:.2f}KB")
    tracemalloc.stop()

if __name__ == "__main__":
    main()