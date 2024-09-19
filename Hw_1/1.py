a = list(map(int, input().split()))
for i in range(0, len(a) - 1, 2):
    b = a[i]
    a[i] = a[i+1]
    a[i+1] = b
print(" ".join(map(str, a)))