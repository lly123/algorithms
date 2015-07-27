__author__ = 'lly'


class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = 0
        self.parent = None

    def sub_tree(self, is_left):
        return self.left if is_left else self.right

    def replace_parent(self, p, ot):
        self.parent = p
        if p is not None:
            if p.left == ot:
                p.left = self
            else:
                p.right = self

    def insert(self, t):
        def handle_rotation(t):
            def rotate_right(t):
                tp = t.parent
                tp.left = t.right
                t.replace_parent(tp.parent, tp)
                tp.replace_parent(t, tp.left)
                return t

            def rotate_left(t):
                tp = t.parent
                tp.right = t.left
                t.replace_parent(tp.parent, tp)
                tp.replace_parent(t, tp.right)
                return t

            def flip_color(t):
                t.left.color = 0
                t.right.color = 0
                t.color = 1 if t.parent is not None else 0
                return t

            if t.parent is None:
                t.color = 0
                return t

            if t.color == 0:
                return handle_rotation(t.parent)
            else:
                if t.parent.color is 0:
                    if t.parent.left is not None and t.parent.left.color is 1 and \
                                    t.parent.right is not None and t.parent.right.color is 1:
                        flip_color(t.parent)
                    return handle_rotation(t.parent)
                else:
                    is_left = t == t.parent.left
                    p_is_left = t.parent == t.parent.parent.left
                    if is_left and p_is_left:
                        t = rotate_right(t.parent)
                        return handle_rotation(flip_color(t))
                    if not is_left and not p_is_left:
                        t = rotate_left(t.parent)
                        return handle_rotation(flip_color(t))
                    if is_left and not p_is_left:
                        t = rotate_right(t)
                        t = rotate_left(t)
                        return handle_rotation(flip_color(t))
                    if not is_left and p_is_left:
                        t = rotate_left(t)
                        t = rotate_right(t)
                        return handle_rotation(flip_color(t))

        is_left = self.key < t.key
        st = self.sub_tree(is_left)

        if st is None:
            if is_left:
                self.left = t
            else:
                self.right = t
            t.parent = self
            t.color = 1
            return handle_rotation(t)
        else:
            return st.insert(t)

    def __repr__(self):
        return "key: %s, color: %d, left: [%s], right: [%s]" % (self.key, self.color, self.left, self.right)


t = Tree(100)
t = t.insert(Tree(200))
t = t.insert(Tree(300))
t = t.insert(Tree(150))
t = t.insert(Tree(80))
t = t.insert(Tree(220))
t = t.insert(Tree(310))
print(t)