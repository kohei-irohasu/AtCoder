# A問題
N = int(input())
S = input()

print('Yes' if 'ab' in S or 'ba' in S else 'No')



#B問題
B = int(input())
ans = -1

for A in range(1, 16):
    if A ** A == B:
        ans = A
        break
    
print(ans)

# B別解
B = int(input())

A = 1
while A ** A <= B:
    if A ** A == B:
        print(A)
        break
    A += 1
else:
    print(-1)
    
    
#C問題
A = [list(map(int, input().split())) for _ in range(9)]
subgrids = [[] for _ in range(9)]

def is_valid(data):
    return all(len(set(row)) == 9 for row in data)

flag = is_valid(A) and is_valid(zip(*A))

for i in range(9):
    for j in range(0, 9, 3):
        subgrids[3 * (i // 3) + j // 3].extend(A[i][j:j+3])

flag = flag and all(len(set(subgrid)) == 9 for subgrid in subgrids)

print('Yes' if flag else 'No')



#D問題