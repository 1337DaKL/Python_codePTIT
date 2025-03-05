def ham(s1, s2):
    list1 = sorted(list(s1))
    list2 = sorted(list(s2))
    return list1 == list2  

if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        s1 = input().strip()
        s2 = input().strip()
        if ham(s1, s2):
            print(f"Test {i + 1}: YES")
        else:
            print(f"Test {i + 1}: NO")