from enum import Enum

PRE = float("-inf")


def judge_bst(tree, node):
    """
    :param tree: 二叉树数组
    :param node: 二叉树结点下标
    :return: 布尔值
    """
    if node >= len(tree) or tree[node] == -1:
        return True
    global PRE
    if not judge_bst(tree, 2 * node + 1) or tree[node] < PRE:
        return False
    PRE = tree[node]
    return judge_bst(tree, 2 * node + 2)


class Color(Enum):
    RED = 1
    BLACK = 2


class RBTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
        self.key = value


class RBT:
    def __init__(self):
        node = RBTNode(0)
        node.color = Color.BLACK
        self.nil = node
        self._root = self.nil

    def get_inorder(self):
        """
        :return: 中序遍历列表，元素为（颜色，key)
        """
        array = []
        self.inorder(self._root, array)
        return array

    def inorder(self, node, array):
        if node == self.nil:
            return
        self.inorder(node.left, array)
        array.append((node.color.name, node.key))
        self.inorder(node.right, array)

    def RBT_insert(self, z):
        y = self.nil
        x = self._root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self._root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = Color.RED
        self.RBT_insert_fixup(z)

    def RBT_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.RBT_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.RBT_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBT_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBT_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self.RBT_delete_fixup(x)

    def RBT_insert_fixup(self, z):
        while z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.left_rotate(z.parent.parent)
        self._root.color = Color.BLACK

    def RBT_delete_fixup(self, x):
        while x != self._root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.left_rotate(x.parent)
                    x = self._root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.right_rotate(x.parent)
                    x = self._root
        x.color = Color.BLACK

    def RBT_transplant(self, u, v):
        if u.parent == self.nil:
            self._root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self._root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x
