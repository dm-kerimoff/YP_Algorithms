def get_max(array, capacity):
    result = 0
    for item in array:
        if capacity == 0:
            break
        max_weight = min(capacity,item[1])
        result += max_weight * item[0]
        capacity -= max_weight
    return result


def main():
    capacity = int(input())
    n = int(input())
    array = []
    for _ in range(n):
        data = list(map(int, input().split()))
        array.append([data[0],data[1]])

    array = sorted(array, key=lambda x: -x[0])
    print(get_max(array, capacity))


if __name__ == '__main__':
    main()