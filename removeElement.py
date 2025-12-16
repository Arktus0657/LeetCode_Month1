class Solution:
  def removeElement(self, nums, val) -> int:
    t = 0
    for i in range(len(nums)):
      if nums[i] != val:
        nums[t] = nums[i]
        t += 1
    return t

sol = Solution()

print(sol.removeElement([3,2,2,3], 3))          # Output: 2
print(sol.removeElement([4, 5, 6, 7, 4, 4], 4))  # Output: 3
print(sol.removeElement([11, 11, 11, 11], 11))  # Output: 0
print(sol.removeElement([9, 7, 22, 7, 7, 3], 7))   # Output: 2

# Output
# 2
# 3
# 0
# 2