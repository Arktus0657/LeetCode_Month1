class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    if divisor == 0:
      raise ZeroDivisionError("division by zero")
    n = len(f'{abs(dividend):b}')
    n_format = '0' + str(n + 1) + 'b'

    A = '0' * (n + 1)
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    Q = format(abs(dividend), f'0{n}b')
    M = format(abs(divisor) & ((1 << (n + 1)) - 1), n_format)
    count = n

    AQ = A + Q
    while count > 0:
      AQ = format((int(AQ, 2) << 1) & ((1 << (n * 2 + 1)) - 1), f'0{n * 2 + 1}b')
      A, Q = AQ[:n + 1], AQ[n + 1:]
      A_int = int(A, 2) - int(M, 2)
      if A_int < 0:
        A = format(int(A, 2), n_format)
        Q = Q[0:-1] + '0'
      else:
        A = format(A_int, n_format)
        Q = Q[0:-1] + '1'
      AQ = A + Q
      count -= 1
    return sign * int(Q, 2)

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

#This is the output for the following program:
# Dividing 10 by 3 yields: 3
# Dividing 7 by -3 yields: -2
# Dividing -2147483648 by 2147483647 yields: -1
# Dividing 1981445587 by 1172010393 yields: 1
# Dividing -2147483648 by -1 yields: 2147483648
# Dividing 100579234 by -555806774 yields: -5