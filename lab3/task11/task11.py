from collections import deque
import time
import tracemalloc

def solve():
    tracemalloc.start()
    start_time = time.time()

    with open('lab3/task11/input.txt', 'r') as f:
        input_lines = f.read().splitlines()
    
    m = int(input_lines[0])
    reactions = {}
    
    for line in input_lines[1:m+1]:
        parts = line.split(' -> ')
        src = parts[0]
        dst = parts[1]
        if src not in reactions:
            reactions[src] = []
        reactions[src].append(dst)
    
    start = input_lines[m+1].strip()
    target = input_lines[m+2].strip()
    
    if start == target:
        with open('lab3/task11/output.txt', 'w') as f:
            f.write('0\n')
        print(f"Time: {time.time() - start_time:.4f}s")
        print(f"Memory: {tracemalloc.get_traced_memory()[1]/1024:.2f}KB")
        tracemalloc.stop()
        return
    
    visited = {}
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    
    found = -1
    while queue:
        current, steps = queue.popleft()
        if current in reactions:
            for neighbor in reactions[current]:
                if neighbor == target:
                    found = steps + 1
                    with open('lab3/task11/output.txt', 'w') as f:
                        f.write(f'{found}\n')
                    print(f"Time: {time.time() - start_time:.4f}s")
                    print(f"Memory: {tracemalloc.get_traced_memory()[1]/1024:.2f}KB")
                    tracemalloc.stop()
                    return
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append((neighbor, steps + 1))
    
    with open('lab3/task11/output.txt', 'w') as f:
        f.write(f'{found}\n')
    
    print(f"Time: {time.time() - start_time:.4f}s")
    print(f"Memory: {tracemalloc.get_traced_memory()[1]/1024:.2f}KB")
    tracemalloc.stop()

solve()