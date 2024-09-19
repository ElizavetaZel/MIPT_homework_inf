a = list(map(int, input().split()))
b = a[0:len(a)-1]
b.insert(0,a[len(a) - 1])
print(" ".join(map(str, b)))