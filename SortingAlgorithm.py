def quick_sort(array, p, r):
    """
    :param array: 待排序数组
    :param p: 待排序数组的开始下标
    :param r: 待排序数组的结束下标
    :return: 无
    """
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


def counting_sort(array_a, array_b, k):
    """
    :param array_a: 待排序数组
    :param array_b: 排序好的数组
    :param k: 待排序数组元素的范围值 + 1
    :return: 无
    """
    mina = min(array_a)
    array_c = [0 for i in range(k)]
    for i in array_a:
        array_c[i-mina] += 1
    for i in range(1, len(array_c)):
        array_c[i] += array_c[i - 1]
    for i in array_a[::-1]:
        array_b[array_c[i-mina]-1] = i
        array_c[i-mina] -= 1


def partition(array, p, r):
    x = array[r]
    j = p - 1
    for i in range(p, r):
        if array[i] <= x:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[j + 1], array[r] = array[r], array[j + 1]
    return j + 1
