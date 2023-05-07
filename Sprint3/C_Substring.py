def substring(sbstr, stroka):
    f = 0
    lsbstr = len(sbstr)
    lstroka = len(stroka)
    if lsbstr > lstroka:
        return False
    for i in range(lstroka):
        if f == lsbstr:
            return True
        if stroka[i] == sbstr[f]:
            f += 1
    return f == lsbstr


def main():
    print(substring(input(), input()))


if __name__ == '__main__':
    main()