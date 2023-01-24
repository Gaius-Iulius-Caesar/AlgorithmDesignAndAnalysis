import SortingAlgorithm
import random

if __name__ == '__main__':
    # 测试快速排序
    print("==================== 测试快速排序 ====================")
    array = [random.randint(0, 100) for i in range(10)]
    print("待排序数组: ", array)
    SortingAlgorithm.quick_sort(array, 0, 8)
    print("排序后数组: ", array)
    # 测试计数排序
    print("==================== 测试计数排序 ====================")
    array_a = [random.randint(0, 100) for i in range(10)]
    print("待排序数组: ", array_a)
    array_b = [0 for i in range(10)]
    SortingAlgorithm.counting_sort(array_a, array_b, max(array_a) + 1)
    print("排序后数组: ", array_b)
