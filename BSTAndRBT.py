PRE = float("-inf")


def judge_bst(tree, node):
    if node >= len(tree) or tree[node] == -1:
        return True
    global PRE
    if not judge_bst(tree, 2 * node + 1) or tree[node] < PRE:
        return False
    PRE = tree[node]
    return judge_bst(tree, 2 * node + 2)
