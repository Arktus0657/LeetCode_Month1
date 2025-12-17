class Solution:
    def strStr(self, haystack: str, needle: str):
        for i in range(len(haystack)):
            if haystack[i]==needle[0] and haystack[i:i+len(needle)]==needle:
                    return i
        return -1
    
sol = Solution()
haystack1 = "sadbutsad"
needle1 = "sad"
haystack2 = "leetcodelong"
needle2 = "leeto"
haystack3 = "hello"
needle3 = "ll"
haystack4 = "aaaaa"
needle4 = "bba"

print(sol.strStr(haystack1, needle1))
print(sol.strStr(haystack2, needle2))
print(sol.strStr(haystack3, needle3))
print(sol.strStr(haystack4, needle4))

#Outputs:
#0
#-1
#2
#-1