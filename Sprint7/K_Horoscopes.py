def get_max_subarray(a,b):
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    res_a, res_b = [],[]
    a_pos, b_pos = len(a), len(b)

    while (a_pos > 0) and (b_pos > 0):
        if a[a_pos-1] == b[b_pos-1]:
            res_a.append(a_pos)
            res_b.append(b_pos)
            a_pos-=1
            b_pos-=1
        else:
            if dp[a_pos-1][b_pos] > dp[a_pos][b_pos-1]:
                a_pos-=1
            else:
                b_pos-=1
    res_a.reverse()
    res_b.reverse()

    if dp[i][j] != 0:
        print(dp[i][j])
        print(*res_a)
        print(*res_b)
    else:
        print(dp[i][j])


def main():
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    get_max_subarray(a,b)


if __name__ == '__main__':
    main()