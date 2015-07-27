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

            if node is None:
                return None

            if node.key1 > self.key1:
                if self.left is not None and is_down:
                    return self.insert(self.left.insert(node, is_down), False)
                elif self.key2 is None:
                    add_value()
                    return None
                else:
                    return Node(self.key1, node, Node(self.key2, self.middle, self.right))
            elif self.key1 >= node.key1 > self.key2:
                if self.middle is not None and is_down:
                    return self.insert(self.middle.insert(node, is_down), False)
                elif self.key2 is None:
                    add_value()
                    return None
                else:
                    return Node(node.key1, Node(self.key1, self.left, node.left), Node(self.key2, node.right, self.right))
            elif node.key1 <= self.key2:
                if self.right is not None and is_down:
                    return self.insert(self.right.insert(node, is_down), False)
                elif self.key2 is None:
                    add_value()
                    return None
                else:
                    return Node(self.key2, Node(self.key1, self.left, self.middle), node)

    def __repr__(self):
        return "{%s}[%s]{%s}[%s]{%s}" % (self.left, self.key1, self.middle, self.key2, self.right)

n = Node(300)
n = n.insert(Node(400)) or n
n = n.insert(Node(350)) or n
n = n.insert(Node(200)) or n
n = n.insert(Node(100)) or n
n = n.insert(Node(250)) or n
print(n)



