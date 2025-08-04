class Node:
    """A node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node):
    """Traverse the tree in pre-order (node, left, right)."""
    if node:
        yield node.value
        yield from preorder(node.left)
        yield from preorder(node.right)


def inorder(node):
    """Traverse the tree in in-order (left, node, right)."""
    if node:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)


def postorder(node):
    """Traverse the tree in post-order (left, right, node)."""
    if node:
        yield from postorder(node.left)
        yield from postorder(node.right)
        yield node.value


def level_order(root):
    """Traverse the tree in level-order (breadth-first)."""
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            yield node.value
            queue.append(node.left)
            queue.append(node.right)


if __name__ == "__main__":
    # Construct a simple binary tree:
    #        A
    #       / \
    #      B   C
    #     / \   \
    #    D   E   F
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.right = Node("F")

    print("Pre-order:", list(preorder(root)))
    print("In-order:", list(inorder(root)))
    print("Post-order:", list(postorder(root)))
    print("Level-order:", list(level_order(root)))
