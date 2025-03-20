class BinaryTree:
    def __init__(self, n):
        """Инициализируем дерево списком из n узлов."""
        self.n = n  
        self.nodes = [None] * n 

    def add_node(self, index, data, left, right):
        """Добавляет узел в дерево."""
        self.nodes[index] = (data, left, right)  

    def in_order_traversal(self, index, result):
        """Рекурсивный обход дерева в порядке in-order."""
        if index == -1:
            return
        data, left, right = self.nodes[index]  

        self.in_order_traversal(left, result)  # Обходим левое поддерево
        result.append(data)  # Добавляем текущий узел в список
        self.in_order_traversal(right, result)  # Обходим правое поддерево

    def pre_order_travelsar(self, index, result1):
        if index == -1:
            return
        data, left, right = self.nodes[index]
        result1.append(data)
        self.pre_order_travelsar(left, result1)
        self.pre_order_travelsar(right, result1)

    def post_order_travelsar(self, index, result2):
        if index == -1:
            return
        data, left, right = self.nodes[index]
        self.post_order_travelsar(left, result2)
        self.post_order_travelsar(right, result2)
        result2.append(data)


def main():

    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        lines = file.readlines() 
    tree = BinaryTree(n)  

    for i in range(n):
        key, left, right = map(int, lines[i].split())
        tree.add_node(i, key, left, right)

    result = []
    tree.in_order_traversal(0, result)  # Запускаем обход от корня (0)

    result1 = []
    tree.pre_order_travelsar(0, result1)

    result2 = []
    tree.post_order_travelsar(0, result2)

    with open("output.txt", "w") as file:
        file.write("In order:\n")
        file.write(" ".join(map(str, result)) + '\n')
        file.write("Pre order:\n")
        file.write(" ". join(map(str, result1)) + '\n')
        file.write("Post order:\n")
        file.write(" ". join(map(str, result2)))

if __name__ == "__main__":
    main()
