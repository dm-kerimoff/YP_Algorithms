def main():
    counter = {}
    n = int(input())
    words = [input() for _ in range(n)]
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    frequency = 0
    for [word, count] in counter.items():
        if count > frequency:
            str = word
            frequency = count
        if count == frequency and str > word:
            str = word

    print(str)


if __name__ == "__main__":
    main()