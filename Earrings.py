def group_reverse(n):
    arr = [1, 2, 3, 4, 5, 6]
    for i in range(0, 6, n):
        arr[i:i + n] = reversed(arr[i:i + n])
    return arr

input("group_reverse(n) reverses [1, 2, 3, 4, 5, 6] in groups of n. Press Enter")
print("    group_reverse(2) = ", group_reverse(2))
print("    group_reverse(3) = ", group_reverse(3))
n = int(input("Group size (try 2 or 3):  "))
guess = input("Guess the result of group_reverse(" + str(n) + "): ")
input("reverse each group of n elements.  Press Enter")
print("    group_reverse(" + str(n) + ") = ", group_reverse(n),  "   Your guess:", guess)