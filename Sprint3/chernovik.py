# 76340061
def binary_search(nums, target, left, right):  # реализация бинарного поиска методом рекурсии
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search(nums, target, left, mid)
    else:
        return binary_search(nums, target, mid + 1, right)


def find_array(nums, target, left, right):
    # поиск массива, в котором присутствует искомый элемент
    # поиск массива, к которому можно применить рекурсивный метод бинарного поиска
    if right - left == 1:
        return [left, right]
    mid = (left + right) // 2
    if nums[left] <= nums[mid]:
        return [left, mid + 1] if nums[left] <= target <= nums[mid] else find_array(nums, target, mid, right)
    if nums[mid] <= target <= nums[-1]:
        return [mid, right]
    else:
        return find_array(nums, target, left, mid)


def broken_search(nums, target):
    left = 0
    right = len(nums)
    arr_borders = find_array(nums, target, left, right)
    return binary_search(nums, target, *arr_borders)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

test()
