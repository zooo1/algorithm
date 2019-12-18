pibo = [[1,0], [0,1]]

for i in range(39):
    pibo.append([pibo[-1][0]+pibo[-2][0], pibo[-1][1]+pibo[-2][1]])

T = int(input())
for t in range(T):
    N = int(input())
    print(pibo[N][0], pibo[N][1])