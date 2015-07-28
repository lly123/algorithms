__author__ = 'richard'


class Node:
    def __init__(self, key, left=None, middle=None):
        self.key1 = key
        self.left = left
        self.middle = middle
        self.parent = None
        self.key2 = None
        self.right = None

    def insert(self, node, is_down=True):
            def add_value():
                if self.key1 > node.key1:
                    self.key2 = node.key1
                    self.middle = node.left
                    self.right = node.middle
                else:
                    self.key2 = self.key1
                    self.key1 = node.key1
                    self.right = self.middle
                    self.left = node.left
                    self.middle = node.middle

            def add_node(branch, node_splitter):
                return self.insert(branch.insert(node, is_down), False) if branch is not None and is_down \
                    else add_value() if self.key2 is None else node_splitter()

            return None if node is None \
                else add_node(self.left, lambda: Node(self.key1, node, Node(self.key2, self.middle, self.right))) if node.key1 > self.key1 \
                else add_node(self.middle, lambda: Node(node.key1, Node(self.key1, self.left, node.left), Node(self.key2, node.right, self.right))) if self.key1 >= node.key1 > self.key2 \
                else add_node(self.right, lambda: Node(self.key2, Node(self.key1, self.left, self.middle), node))

    def __repr__(self):
        return "[%s] [%s]" % (self.key1, self.key2) + "\n{%s} {%s} {%s}\n" % (self.left, self.middle, self.right)

n = Node(300)
n = n.insert(Node(400)) or n
n = n.insert(Node(350)) or n
n = n.insert(Node(200)) or n
n = n.insert(Node(100)) or n
n = n.insert(Node(250)) or n
n = n.insert(Node(50)) or n
n = n.insert(Node(220)) or n
n = n.insert(Node(310)) or n
print(n)




