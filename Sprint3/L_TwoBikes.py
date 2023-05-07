def binary_search(arr, price, left, right):
    if right <= left or price > arr[right - 1]:
        return -1
    mid = (left + right) // 2
    if (arr[mid] >= price and mid == left) or (arr[mid] >= price > arr[mid - 1]):
        return mid + 1
    elif price > arr[mid]:
        return binary_search(arr, price, mid+1, right)
    else:
        return binary_search(arr, price, left, mid)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    price = int(input())
    day1 = binary_search(arr, price, 0, len(arr))
    day2 = binary_search(arr, price * 2, 0, len(arr))
    print(day1, day2)


if __name__ == '__main__':
    main()
