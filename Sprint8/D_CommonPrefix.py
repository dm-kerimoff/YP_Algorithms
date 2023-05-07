def GetMaxPrefixLen(words):
    if len(words) == 0:
        return 0

    first_word = words[0]
    for ln in range(len(first_word)):
        for i in range(1, len(words)):
            if ln == len(words[i]):
                return ln

            if words[i][ln] != first_word[ln]:
                return ln
    return ln+1


def main():
    n = int(input())
    words = sorted([(input()) for _ in range(n)],key=len)
    print(GetMaxPrefixLen(words))


if __name__ == '__main__':
    main()