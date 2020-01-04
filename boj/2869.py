A, B, V = map(int, input().split())
if A>=V:
    print(1)
else:
    if (V-A)//(A-B) != (V-A)/(A-B):
        print(2+(V-A)//(A-B))
    else:
        print((V-A)//(A-B)+1)
