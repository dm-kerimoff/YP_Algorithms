def fun(n, k, form):
    form = int(form.replace(' ', ''))
    return ' '.join(list(str(form + k)))

n = int(input())
form = input()
k = int(input())
print(fun(n, k, form))
