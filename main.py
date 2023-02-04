import numpy as np
import DivideAndConquer
import SortingAlgorithm
import OptimalTaskScheduling
import BSTAndRBT
import Backpack_01

if __name__ == '__main__':
    # 测试最大子数组和
    print("================== 测试最大子数组和 ===================")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("最大子数组和为: ", DivideAndConquer.max_subarray(nums, 0, len(nums) - 1))
    # 测试快速排序
    print("=================== 测试快速排序 =====================")
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("待排序数组: ", array)
    SortingAlgorithm.quick_sort(array, 0, len(array) - 1)
    print("排序后数组: ", array)
    # 测试计数排序
    print("=================== 测试计数排序 =====================")
    array_a = [95, 94, 91, 98, 99, 90, 99, 93, 91, 92]
    print("待排序数组: ", array_a)
    array_b = [0 for i in range(len(array_a))]
    SortingAlgorithm.counting_sort(array_a, array_b, max(array_a) - min(array_a) + 1)
    print("排序后数组: ", array_b)
    # 测试二叉查找树
    print("=================== 测试二叉查找树 ====================")
    tree = [5, 1, 4, -1, -1, 3, 6]
    print("输入: ", tree, "\n结果: ", BSTAndRBT.judge_bst(tree, 0))
    # 测试红黑树
    print("==================== 测试红黑树 ======================")
    key_input = [1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    key_delete = [14, 9, 5]
    key_delete_node = [BSTAndRBT.RBTNode(0) for i in key_delete]
    print("依次插入:", key_input)
    rbt = BSTAndRBT.RBT()
    for i in key_input:
        rbtNode = BSTAndRBT.RBTNode(i)
        rbt.RBT_insert(rbtNode)
        if i in key_delete:
            key_delete_node[key_delete.index(i)] = rbtNode
    print("中序遍历结果:\n", np.array(rbt.get_inorder()))
    for node in key_delete_node:
        rbt.RBT_delete(node)
        print("删除", node.key, "结果为:\n", np.array(rbt.get_inorder()))
    # 测试最佳任务调度
    print("================== 测试最佳任务调度 ===================")
    d = [4, 2, 4, 3, 1, 4, 6]
    w = [70, 60, 50, 40, 30, 20, 10]
    print("调度结果: ", end='')
    for task_index in OptimalTaskScheduling.task_scheduling(d, w)[0]:
        print("a{}".format(task_index), end=' ')
    print("—— 惩罚值:", OptimalTaskScheduling.task_scheduling(d, w)[1])
    new_w = [max(w) - i for i in w]
    print("替换惩罚值之后的调度结果: ", end='')
    for task_index in OptimalTaskScheduling.task_scheduling(d, new_w)[0]:
        print("a{}".format(task_index), end=' ')
    print("—— 惩罚值:", OptimalTaskScheduling.task_scheduling(d, new_w)[1])
    # 测试01背包问题
    print("================== 测试01背包问题 ====================")
    n = int(input("请输入物品数量: "))
    c = int(input("请输入背包容量: "))
    w = [int(i) for i in input("请输入物品重量数组，以逗号分割: ").split(',')]
    v = [int(i) for i in input("请输入物品价值数组，以逗号分割: ").split(',')]
    print("使用动态规划得到最大价值为: ", Backpack_01.dp_solve(n, c, w, v))
    print("使用回溯法得到最大价值为: ", Backpack_01.bp_solve(n, c, w, v))
