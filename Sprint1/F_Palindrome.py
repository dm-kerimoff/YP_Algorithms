def palindrom(str):
    str = str.lower()
    m = ' ,;!&?.:-=%+'
    for j in m:
        str = str.replace(j,'')
    return str == str[::-1]

str = input()
print(palindrom(str))
