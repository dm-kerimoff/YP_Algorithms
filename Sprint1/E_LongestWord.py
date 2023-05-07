n = int(input())
str = input()
str.strip()
words = str.split()
max = imax = 0
for i in range(len(words)):
    if len(words[i]) > max:
        max = len(words[i])
        imax = i
print(words[imax])
print(len(words[imax]))
