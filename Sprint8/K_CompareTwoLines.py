def symb_del(st, even_symb):
    return ''.join(c for c in st if c in even_symb)


def main():
    even_symb = {'b','d','f','h','j','l','n','p','r','t','v','x','z'}
    a,b = symb_del(input(), even_symb), symb_del(input(), even_symb)
    if a < b:
        print(-1)
    elif a == b:
        print(0)
    else:
        print(1)


if __name__ == "__main__":
    main()