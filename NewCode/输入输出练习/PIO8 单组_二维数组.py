n, m = map(int, input().split())

total_sum = 0
for _ in range(n):
    row = list(map(int, input().split()))
    total_sum += sum(row)

print(total_sum)
