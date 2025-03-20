import sys
import tracemalloc
import time

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def build_tree(n, nodes):
    tree = [None] * (n + 1)
    for i in range(1, n + 1):
        key, left, right = nodes[i - 1]
        if tree[i] is None:
            tree[i] = TreeNode(key)
        else:
            tree[i].key = key
        if left != 0:
            tree[left] = TreeNode(None)
            tree[left].parent = tree[i]
            tree[i].left = tree[left]
        if right != 0:
            tree[right] = TreeNode(None)
            tree[right].parent = tree[i]
            tree[i].right = tree[right]
    return tree[1]

def delete_subtree(root, key):
    if root is None:
        return root
    if root.key == key:
        return None
    if key < root.key:
        root.left = delete_subtree(root.left, key)
    else:
        root.right = delete_subtree(root.right, key)
    return root

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def main():
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
    m = int(input_data[ptr])
    ptr += 1
    delete_keys = list(map(int, input_data[ptr:ptr + m]))
    
    root = build_tree(n, nodes)
    
    with open("output.txt", "w") as f:
        for key in delete_keys:
            root = delete_subtree(root, key)
            f.write(f"{count_nodes(root)}\n")
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time:.4f} секунд")
    print(f"Пиковое использование памяти: {peak / 1024 / 1024:.4f} МБ")

if __name__ == "__main__":
    main()