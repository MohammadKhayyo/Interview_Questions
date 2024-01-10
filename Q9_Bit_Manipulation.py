# 9. Bit Manipulation:
# • Write a program to check if a given number is even or odd using bit manipulation.
def isEven(n):
    # n^1 is n+1, then even, else odd
    if (n ^ 1) == (n + 1):
        return True
    else:
        return False


# • Write a program to find the number of set bits in a given integer using bit manipulation
#  The Hamming weigh
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1  # Flip the least significant set bit
        count += 1
    return count


def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


if __name__ == "__main__":
    # 9. Bit Manipulation:
    # • Write a program to check if a given number is even or odd using bit manipulation.
    _n = 196
    print("Even") if isEven(_n) else print("Odd")
    _n = 19
    print("Even") if isEven(_n) else print("Odd")

    # • Write a program to find the number of set bits in a given integer using bit manipulation
    number = 29  # Binary representation of 29 is 11101, which has four set bits
    print(f"Number of set bits in {number}: {count_set_bits(number)}")
    number = 29  # Binary representation of 29 is 11101, which has four set bits
    print(f"Number of set bits in {number}: {countSetBits(number)}")
