def get_path(dp,array,n,m):
    for i in range(n):
        for j in range(m):
            y = n-i-1
            x = j
            down = 0
            if y + 1 != n:
                down = dp[y+1][x]
            left = 0
            if x != 0:
                left = dp[y][x-1]
            dp[y][x] = max(left,down)+array[y][x]

    print(dp[0][m-1])

    y = 0
    x = m - 1
    path = ''
    while y != n or x != 0:
        if x == 0:
            path += 'U'
            y += 1
            continue
        down = 0
        if y + 1 < n:
            down = dp[y+1][x]
        left = 0
        if x > 0:
            left = dp[y][x-1]
        if down > left:
            y += 1
            path += 'U'
        else:
            x -= 1
            path += 'R'
    path = path[:-1]
    return path[::-1]


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    array = [list(map(int,list(input()))) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    print(get_path(dp,array,n,m))


if __name__ == '__main__':
    main()