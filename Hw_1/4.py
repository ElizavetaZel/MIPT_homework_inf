a = list(map(int, input().split()))
mx = 0
ind = 0
for i in range(0, len(a)):
    if a.count(a[i]) > mx:
        mx = a.count(a[i])
        ind = i
print(a[ind])