A, B = input().split()

minA = minB = maxA = maxB = ''
for a in A:
    if a == '5' or a == '6':
        minA += '5'
        maxA += '6'
    else:
        minA += a
        maxA += a

for b in B:
    if b == '5' or b == '6':
        minB += '5'
        maxB += '6'
    else:
        minB += b
        maxB += b

print(int(minA)+int(minB), int(maxA)+int(maxB))

