n = int(input())
count = 0
def solve():
    x,y,z = list(map(int,input().split()))
    if x+y+z >=2:
        return 1
    return 0
    
for i in range(n):
    count+=solve()
print(count)
