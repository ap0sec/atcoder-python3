N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]


def check(x):
    s = set()
    for a in A:
        print(f"a={a}")
        s.add(sum(1 << i for i in range(5) if a[i] >= x))

    print(s)
    for x in s:
        for y in s:
            for z in s:
                print(f"{x}, {y}, {z}")
                if x | y | z == 31:
                    return True
    return False


ok = 0
ng = 10**9 + 1
while ng - ok > 1:
    cen = (ok + ng) // 2
    print(f"cen = {cen}")
    res = check(cen)
    print(f"res={res}")
    if res:
        ok = cen
    else:
        ng = cen
print(ok)
