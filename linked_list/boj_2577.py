from tabnanny import check

a = 150
b = 266
c = 427

multi = list(str(a * b * c))

for i in range(10):
    print(multi.count(str(i)))  # 17037300


# or

multi2  =a * b * c
counts = [0] * 10 # 0 ~ 9 까지의 개수를 담은 배열 공간 확보
for digit in str(multi2):
    counts[int(digit)] += 1 # 숫자에 해당하는 인덱스의 값을 1 증사

for n in counts:
    print(n)