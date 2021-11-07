def rot(num):
    i = iter(num)
    B = list(iter(lambda: int(next(i)), None))
    for i in range (len(B)):
        if B[i] == 6:
            B[i] = 9
            break
    R = ''.join(str(n) for n in B)
    return R

num = input('num = ', )
print(rot(num))
