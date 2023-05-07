def compare(obj1, obj2):
    return (obj1 + obj2) > (obj2 + obj1)


def fun_sort(array, key):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and key(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return ''.join(array)


def main():
    n = int(input())
    arr = input().split()
    print(fun_sort(arr, compare))


if __name__ == '__main__':
    main()
