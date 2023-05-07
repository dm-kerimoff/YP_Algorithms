def get_max_coins(nominals, x, dp):
    for current_sum in range(1,x+1):
        dp[current_sum] = float('inf')
        for nominal in nominals:
            if nominal <= current_sum:
                dp[current_sum] = min(dp[current_sum], dp[current_sum-nominal] + 1)

    return -1 if dp[x] in [0, float('-inf')] else dp[x]


def main():
    x = int(input())
    k = int(input())
    nominals = list(map(int, input().split()))
    dp = [0] * (x+1)
    print(get_max_coins(nominals, x, dp))


if __name__ =='__main__':
    main()