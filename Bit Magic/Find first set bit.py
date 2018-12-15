# author : vishnugopireddy
# find first set bit from right


def findfirstSetbit(num):
    pos = 1

    # counting the position of first set bit
    for i in range(32):
        if not (num & (1 << i)):
            pos += 1
        else:
            break
    if pos > 32:
        return 0
    else:
        return pos


kases = int(input())
for kase in range(kases):
    num = int(input())
    print(findfirstSetbit(num))
