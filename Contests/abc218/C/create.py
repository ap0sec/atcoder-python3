import random

N = 200


def main():
    print(N)

    R = []

    for i in range(N):
        s = ''
        for j in range(N):
            r = random.randrange(2)
            if r:
                s += '.'
            else:
                s += '#'
        print(s)
        R.append(s)

    R = rotate(N, R)
    R = rotate(N, R)
    R = rotate(N, R)

    for i in R:
        print(i)

def rotate(N: int, t: "List[str]"):

    r = [''] * N
    
    for i in range(N):
        for j in range(N)[::-1]:
            r[i] += t[j][i]

    return r

if __name__ == "__main__":
    main()

