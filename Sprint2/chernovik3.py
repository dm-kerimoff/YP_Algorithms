
def recurs(digits, code, result, f=''):
    if len(f) == len(digits):
        return result.append(f)

    for letter in code[int(digits[len(f)])]:
        recurs(digits, code, result, f+letter)
    return result


def main():
    code = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    digits = input()
    result = []
    print(*recurs(digits, code, result))


if __name__ == '__main__':
    main()