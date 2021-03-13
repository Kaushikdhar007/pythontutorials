print(" How many rows you want to print")
m = int(input())
print("Press 1 or 0\n")

n = bool(int(input()))
if n == True:
    while (n <= m):
        print("*" * (n))
        n = n + 1
        continue
elif n == False:
    while (n <= m):
        print("*" * (m))
        m = m - 1
        continue
