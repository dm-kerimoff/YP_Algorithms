def last_sym(s,t):
    i = 0
    while i < len(s):
        if s[i] == t[i]:
            i += 1
        else:
            break
    return t[i]

s, t = sorted(input()), sorted(input())
print(last_sym(s,t))
