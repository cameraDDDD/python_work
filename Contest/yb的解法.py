def odd_find(n):
    k = 2
    while k * k <= n:
        if (n % k == 0):
            a = k
            b = n - k
            return (True, a, b)
        k += 1
    return (False, 0, 0)

def find_one(l, r):
    for k in range(l, r+1):
        if k != 2 and k % 2 == 0:
            a = k // 2
            b = a
            return (True, a, b)
    return odd_find(l)

def main():
    t = int(input())
    for i in range(t):
        l, r = input().split()
        l = int(l)
        r = int(r)
        success, a, b = find_one(l, r)
        if success:
            print(a, b)
        else:
            print(-1)

if __name__ == "__main__":
    main()