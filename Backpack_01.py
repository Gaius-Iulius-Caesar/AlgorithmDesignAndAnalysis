def dp_solve(n, c, w, v):
    """
    :param n: 物品数量
    :param c: 背包容量
    :param w: 物品重量数组
    :param v: 物品价值数组
    :return: 最大价值总和
    """
    dp = [0 for i in range(c + 1)]
    for i in range(n):
        for j in range(c, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[c]


max_v = 0
current_w = 0
current_v = 0


def bp_solve(n, c, w, v):
    """
    :param n: 物品数量
    :param c: 背包容量
    :param w: 物品重量数组
    :param v: 物品价值数组
    :return: 最大价值总和
    """
    # 按单位价值排序
    order = [i for i in range(n)]
    order = sorted(order, key=lambda i: v[i] / w[i], reverse=True)
    ordred_w = [w[order[i]] for i in range(n)]
    ordred_v = [v[order[i]] for i in range(n)]
    bp(0, n, c, ordred_w, ordred_v)
    return max_v


def bp(k, n, c, ordred_w, ordred_v):
    """
    :param k: 递归层数
    :param n: 物品数量
    :param c: 背包容量
    :param ordred_w: 已排序的物品重量数组
    :param ordred_v: 已排序的物品价值数组
    :return: 最大价值
    """
    global max_v
    global current_v
    global current_w
    if k >= n:
        max_v = current_v
        return
    # 左子树
    if current_w + ordred_w[k] <= c:
        current_w += ordred_w[k]
        current_v += ordred_v[k]
        bp(k + 1, n, c, ordred_w, ordred_v)
        current_w -= ordred_w[k]
        current_v -= ordred_v[k]
    # 右子树
    if bound(k + 1, n, c, ordred_w, ordred_v) > max_v:
        bp(k + 1, n, c, ordred_w, ordred_v)


def bound(k, n, c, ordred_w, ordred_v):
    """
    :param k: 递归层数
    :param n: 物品数量
    :param c: 背包容量
    :param ordred_w: 已排序的物品重量数组
    :param ordred_v: 已排序的物品价值数组
    :return: 价值上界
    """
    global current_w
    global current_v
    left_w = c - current_w
    max_predict_v = current_v
    while k < n and ordred_w[k] < left_w:
        left_w -= ordred_w[k]
        max_predict_v += ordred_v[k]
        k += 1
    if k < n:
        max_predict_v += ordred_v[k] / ordred_w[k] * left_w
    return max_predict_v
