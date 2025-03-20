import sys
import time
import tracemalloc

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(n, nodes):
    tree = [None] * (n + 1)
    for i in range(1, n + 1):
        key, left, right = nodes[i - 1]
        if tree[i] is None:
            tree[i] = TreeNode(key)
        if left != 0:
            if tree[left] is None:
                tree[left] = TreeNode(None)  # Инициализация с None
            tree[i].left = tree[left]
        if right != 0:
            if tree[right] is None:
                tree[right] = TreeNode(None)  # Инициализация с None
            tree[i].right = tree[right]
    return tree[1]

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None or root.key is None:
        return True
    if not (min_val < root.key < max_val):
        return False
    return (is_bst(root.left, min_val, root.key) and
            is_bst(root.right, root.key, max_val))

def main():
    # Начинаем замер памяти
    tracemalloc.start()
    start_time = time.time()

    with open("input.txt", "r") as f:
        input_data = f.read().split()
    
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = []
    for _ in range(n):
        key = int(input_data[ptr])
        left = int(input_data[ptr + 1])
        right = int(input_data[ptr + 2])
        nodes.append((key, left, right))
        ptr += 3
    
    if n == 0:
        with open("output.txt", "w") as f:
            f.write("YES\n")
        return
    
    root = build_tree(n, nodes)
    
    with open("output.txt", "w") as f:
        if is_bst(root):
            f.write("YES\n")
        else:
            f.write("NO\n")
    
    # Замер времени и памяти
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Пиковое использование памяти: {peak / 1024 / 1024:.6f} МБ")

if __name__ == "__main__":
    main()