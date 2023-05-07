
def get_max_arr(data):
    mx = 0
    dp = [1 for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j]+1)
        mx = max(mx, dp[i])

    positions, subarray = [],[]
    print(mx)

    for i in range(len(dp)-1,-1,-1):
        if mx == dp[i] and (not positions or data[i] < subarray[-1]):
            subarray.append(data[i])
            positions.append(i+1)
            mx -= 1

    positions.reverse()
    if positions:
        print(*positions)




def main():
    n = int(input())
    data = list(map(int,input().split()))
    get_max_arr(data)


if __name__ == '__main__':
    main()