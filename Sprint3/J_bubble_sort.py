def bubble_sort(nums):
    # Установим swapped в True, чтобы цикл запустился хотя бы раз
    swapped = True
    k = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Установим swapped в True для последующей итерации
                swapped = True
                k += 1
        if swapped == True:
            print(*nums)
    if swapped == False and k == 0:
        print(*nums)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr)

if __name__ == '__main__':
    main()




