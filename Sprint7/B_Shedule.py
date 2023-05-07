def main():
    array = []
    n = int(input())
    for _ in range(1, n+1):
        data = input().split()
        array.append([int(float(data[0])) if int(float(data[0])) == float(data[0]) else float(data[0]),int(float(data[1])) if int(float(data[1])) == float(data[1]) else float(data[1])])

    array = sorted(array, key=lambda x: [x[1], x[0]])

    result = [array[0]]
    C = 1

    for i in range(1, len(array)):
        if array[i][0] >= result[-1][1]:
            result.append((array[i]))
            C += 1

    print(C)
    for item in result:
        print(*item)


if __name__ == '__main__':
    main()