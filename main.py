import SortingAlgorithm

if __name__ == '__main__':
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
