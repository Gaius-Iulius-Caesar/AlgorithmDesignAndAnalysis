def findMedianSortedArrays(nums1, nums2):
    def getKthElement(k):
        index1, index2 = 0, 0
        while True:
            # 特殊情况
            if index1 == m:  # nums1被排除
                return nums2[index2 + k - 1]
            if index2 == n:  # nums2被排除
                return nums1[index1 + k - 1]
            if k == 1:  # 寻找第1小的元素
                return min(nums1[index1], nums2[index2])
            # 正常情况
            newIndex1 = min(index1 + k // 2 - 1, m - 1)
            newIndex2 = min(index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
            if pivot1 <= pivot2:
                k -= (newIndex1 - index1 + 1)  # 减去已排除的元素数
                index1 = newIndex1 + 1  # 此下标之前的元素已排除
            else:
                k -= (newIndex2 - index2 + 1)  # 减去已排除的元素数
                index2 = newIndex2 + 1  # 此下标之前的元素已排除

    m, n = len(nums1), len(nums2)
    totalLength = m + n
    if totalLength % 2 == 1:
        return getKthElement((totalLength + 1) // 2)
    else:
        return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


def max_subarray(nums, left, right):
    """
    :param nums: 数组
    :param left: 左端点下标
    :param right: 右端点下标
    :return: 最大子数组和
    """
    if left == right:
        return nums[left]
    mid = (left + right) >> 1
    return max(max_subarray(nums, left, mid), max_subarray(nums, mid + 1, right),
               max_cross_array(nums, left, mid, right))


def max_cross_array(nums, left, mid, right):
    """
    :param nums: 数组
    :param left: 左端点下标
    :param mid: 中间位置下标
    :param right: 右端点下标
    :return: 跨越中间的最大子数组和
    """
    left_sum_max = 0
    start_left = mid - 1
    s1 = 0
    while start_left >= left:
        s1 += nums[start_left]
        left_sum_max = max(left_sum_max, s1)
        start_left -= 1

    right_sum_max = 0
    start_right = mid + 1
    s2 = 0
    while start_right <= right:
        s2 += nums[start_right]
        right_sum_max = max(right_sum_max, s2)
        start_right += 1
    return left_sum_max + nums[mid] + right_sum_max
