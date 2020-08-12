#problrm here -> https://www.hackerrank.com/challenges/py-set-mutations/problem

a = int(raw_input())
A = set(map(int, raw_input().split()))
for i in range(int(input())):
    s, b = raw_input().split()
    if s == 'intersection_update':
        A &= set(map(int, raw_input().split()))
    elif s == 'update':
        A |= set(map(int, raw_input().split()))
    elif s == 'symmetric_difference_update':
        A ^= set(map(int, raw_input().split()))
    else:
        A -= set(map(int, raw_input().split()))
print(sum(A))
