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
