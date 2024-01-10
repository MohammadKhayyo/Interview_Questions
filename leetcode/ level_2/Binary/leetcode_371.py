"""Sum of Two Integers"""
"""Link to the problem: https://leetcode.com/problems/sum-of-two-integers/"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a


"""
In java
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
                int tmp = (a & b) << 1;
                a = a ^ b;
                b = tmp;
            }
            return a;
    }
}
"""
if __name__ == '__main__':
    solution = Solution()
    Input = {"a": 1, "b": 2}
    print(f"Input:{Input}")
    Output = solution.getSum(Input["a"], Input["b"])
    print(f"Output:{Output}")
    print(len("11111111111111111111111111111111"))
    print(len("10000000000000000000000000000000"))
    print()
    print(10000000000000000000000000000000 & 0xffffffff)  # 2147483648
    print(10000000000000000000000000000000 & 11111111111111111111111111111111)  # 967351160499599029774602731520
    binary = '10000000000000000000000000000000'
    decimal = int(binary, 2)
    print(decimal)  # Output: 2147483648
