# ID 72148984
def fast_hands(k):
    d = {}
    for _ in range(4):
        s = input()
        for c in s:
            if c != '.':
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
    return sum(i <= 2 * k for i in d.values())


def main():
    k = int(input())
    print(fast_hands(k))


if __name__ == "__main__":
    main()
