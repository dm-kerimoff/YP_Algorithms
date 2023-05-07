"""
Пока цена следующего дня больше предыдущего, то будем продавать акцию
"""

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    profit = sum(prices[i] - prices[i - 1] for i in range(1, n) if prices[i - 1] < prices[i])
    print(profit)


if __name__ == '__main__':
    main()