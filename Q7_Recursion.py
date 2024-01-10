# Recursion
# • Write a program to calculate the factorial of a number using recursion.
def factorial(n):
    # Checking the number is 1 or 0 then return 1 otherwise return factorial
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# • Write a program to generate all permutations of a string using recursion.
def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)


if __name__ == '__main__':
    # Recursion
    # • Write a program to calculate the factorial of a number using recursion.
    num = 5
    print("number : ", num)
    print("Factorial : ", factorial(num))

    # • Write a program to generate all permutations of a string using recursion.
    string = "ABCDE"
    n = len(string)
    a = list(string)
    # Function call
    permute(a, 0, n)
