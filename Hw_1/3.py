a = list(map(int, input().split()))
for i in range(0, len(a), 1):
    if a.count(a[i]) == 1:
        print(a[i])