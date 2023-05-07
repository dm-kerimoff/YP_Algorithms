def main():
    data = list(map(int, input().split()))
    n, k = data[0], data[1]
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        for j in range(max(0, i-k), i):
            dp[i] = (dp[i] + dp[j]) % 1000000007
    print(dp[n-1])


if __name__ == '__main__':
    main()

