# ATM
import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().rstrip().split()))
time.sort()

sum, result = 0, 0

for i in range(n):
    sum += time[i]
    result += sum

print(result)