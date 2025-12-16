class Solution:
  def romanToInt(self, s: str) -> int:
    roman = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 100
    }
    num = 0
    for i in range(len(s)):
      if (i + 1) < len(s) and roman[s[i]] < roman[s[i + 1]]:
        num -= roman[s[i]]
      else:
        num += roman[s[i]]
    return num
sol = Solution()

s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"
s4 = "CDLXIX"
s5 = "CDLXXXVIII"
s6 = "CDXLIX"
print(f"Roman numeral {s1} converts to integer: {sol.romanToInt(s1)}")
print(f"Roman numeral {s2} converts to integer: {sol.romanToInt(s2)}")
print(f"Roman numeral {s3} converts to integer: {sol.romanToInt(s3)}")
print(f"Roman numeral {s4} converts to integer: {sol.romanToInt(s4)}")
print(f"Roman numeral {s5} converts to integer: {sol.romanToInt(s5)}")
print(f"Roman numeral {s6} converts to integer: {sol.romanToInt(s6)}")

# Output
# Roman numeral III converts to integer: 3
# Roman numeral LVIII converts to integer: 58
# Roman numeral MCMXCIV converts to integer: 394
# Roman numeral CDLXIX converts to integer: 469
# Roman numeral CDLXXXVIII converts to integer: 488
# Roman numeral CDXLIX converts to integer: 449