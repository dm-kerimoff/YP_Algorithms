def compare(obj1, obj2):
    return obj1[0] < obj2[0] if (obj1[1] == obj2[2]) else obj1[1] > obj2[1]


def insertion_sort(array, more):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and more(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return array


def GetTop(arr, n, k):
    d = {}
    for val in arr:
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1

    res = insertion_sort(list(d.items()), compare)
    return [res[1] for _ in range(k)]


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(GetTop(arr, n, k))


if __name__ == '__main__':
    main()