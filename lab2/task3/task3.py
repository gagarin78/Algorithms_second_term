class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        cur, parent = self.root, None
        while cur:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return
        if key < parent.key:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

    def find_min_greater(self, key):
        cur, successor = self.root, None
        while cur:
            if cur.key > key:
                successor = cur
                cur = cur.left
            else:
                cur = cur.right
        return successor.key if successor else 0


def main():
    bst = BST()
    output = []

    with open("input.txt", "r") as infile:
        for line in infile:
            command, value = line[0], int(line[2:])
            if command == "+":
                bst.insert(value)
            elif command == ">":
                output.append(str(bst.find_min_greater(value)))

    with open("output.txt", "w") as outfile:
        outfile.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
