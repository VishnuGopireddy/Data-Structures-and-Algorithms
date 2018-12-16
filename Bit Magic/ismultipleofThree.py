# author : vishnugopireddy
# Check given binary number is a multiple of 3 or not
def ismultipleofThree(arr):
    even = arr[1::2]
    odd = arr[::2]
    even = [int(i) for i in even]
    odd = [int(i) for i in odd]
    if abs(sum(even)-sum(odd)) % 3 == 0:
        return 1
    else:
        return 0

kases = int(input())
for kase in range(kases):
    arr = input()
    print(ismultipleofThree(arr))