n, m = map(int, input().split())

for i in range(1,min(n,m)+1):

    if n % i == 0 and m % i == 0:
        lcm = i * (n//i) * (m//i)
        gcd = i

print(gcd)
print(lcm)