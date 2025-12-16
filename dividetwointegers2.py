#Creating a leaner solution to the same problem
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Scope Constraint Handling
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        # Unsigned Division
        A, M = abs(dividend), abs(divisor)
        quotient = 0

        while A >= M:
            temp = M
            pwr = 1

            # Subtracting max power of two multiple of divisor from dividend
            while A >= (temp << 1):
                temp <<= 1
                pwr <<= 1
            A -= temp
            quotient += pwr

        # Giving sign
        if (dividend > 0) != (divisor > 0):
            return -quotient
        return quotient

sol = Solution()

dividend1 = 10
divisor1 = 3
dividend2 = 7
divisor2 = -3
dividend3 = -2147483648
divisor3 = 2147483647
dividend4 = 1981445587
divisor4 = 1172010393
dividend5 = -2147483648
divisor5 = -1
dividend6 = 100579234
divisor6 = -555806774

print(f"Dividing {dividend1} by {divisor1} yields: {sol.divide(dividend1, divisor1)}")
print(f"Dividing {dividend2} by {divisor2} yields: {sol.divide(dividend2, divisor2)}")
print(f"Dividing {dividend3} by {divisor3} yields: {sol.divide(dividend3, divisor3)}")
print(f"Dividing {dividend4} by {divisor4} yields: {sol.divide(dividend4, divisor4)}")
print(f"Dividing {dividend5} by {divisor5} yields: {sol.divide(dividend5, divisor5)}")
print(f"Dividing {dividend6} by {divisor6} yields: {sol.divide(dividend6, divisor6)}")

#Output
# Dividing 10 by 3 yields: 3
# Dividing 7 by -3 yields: -2
# Dividing -2147483648 by 2147483647 yields: -1
# Dividing 1981445587 by 1172010393 yields: 1
# Dividing -2147483648 by -1 yields: 2147483647
# Dividing 100579234 by -555806774 yields: 0