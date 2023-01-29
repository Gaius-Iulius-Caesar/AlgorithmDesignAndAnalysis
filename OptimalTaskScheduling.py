def task_scheduling(d, w):
    """
    :param d: 截止时间数组(1 <= d[i] <= n)
    :param w: 惩罚数组
    :return: 调度结果和惩罚值
    """
    # a数组保存按惩罚降序排序的任务编号（从1开始)
    a = sorted(range(1, len(d) + 1), key=lambda i: w[i - 1], reverse=True)
    advance = []  # 提前数组
    defer = []  # 延迟数组
    for task_index in a:
        # 验证独立性, 先加入提前数组
        advance.append(task_index)
        # N[t] 表示截止时间小于等于t的任务数
        N = [0 for i in range(len(advance) + 1)]
        for advance_task_index in advance:
            if d[advance_task_index - 1] >= len(N):
                N[-1] += 1
            else:
                N[d[advance_task_index - 1]] += 1
        for i in range(1, len(N)):
            N[i] += N[i - 1]
        # 检查是否存在Nt(advance) > t, 如果存在从提前数组中删除，放入延迟数组
        for t in range(len(N)):
            if N[t] > t:
                defer.append(advance.pop())
    # 将提前数组转为规范形式
    advance.sort(key=lambda i: d[i - 1])
    # 返回结果
    return advance + defer, sum([w[task_index-1] for task_index in defer])
