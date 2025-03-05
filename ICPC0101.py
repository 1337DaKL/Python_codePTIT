n = int(input())
arr = list(map(int , input().split()))
stack = []
for i in arr:
    if len(stack) == 0:
        stack.append(i)
    else:
        last = stack.pop()
        if (i + last) % 2 != 0:
            stack.append(last)
            stack.append(i)
print(len(stack))
# 5
# 2 3 4 5 6
# 10
# 1 5 5 8 6 4 3 5 9 3