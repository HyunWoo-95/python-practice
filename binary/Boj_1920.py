def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


n = 5
a = [4, 1, 5, 2, 3]
a.sort()
m = 5
b = [1,3,7,9,5]

for target in b:
    print(binary_search(target, a))
