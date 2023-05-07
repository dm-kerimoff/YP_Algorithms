def OneEditDistance(lstr, rstr):
    if abs(len(lstr) - len(rstr)) > 1:
        return False

    if len(lstr) > len(rstr):
        return OneEditDistance(rstr, lstr)

    lstr_pos = rstr_pos = 0
    one_diff = False

    while lstr_pos < len(lstr) and rstr_pos < len(rstr):
        if lstr[lstr_pos] != rstr[rstr_pos]:
            if one_diff:
                return False
            one_diff = True

            if len(lstr) == len(rstr):
                lstr_pos += 1
        else:
            lstr_pos += 1
        rstr_pos += 1
    return True


def main():
    lstr, rstr = input(), input()
    if OneEditDistance(lstr, rstr):
        print('OK')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()