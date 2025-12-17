> Initializing Commit
# LeetCode_Month1.ipynb Creation
This is the first month of uploading my leetcode practicing to github in a ipynb style

> First Commit
# First Question:
Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

> Second Commit
# Approach: 
1. We are using the classic restoring division algorithm but summing the accumulator to the dividend(quotient) and assign the count as length of dividend. Handle the scope issues too.
2. We Shift left the sum of accumulator and quotient. 
3. Then after splitting them back. 
4. We subtract the accumulator by the divisor.
5. If the sign of the divisor is positive then we assign the last bit of quotient to 1.
6. If the sign of the divisor is negative then we assign the last bit of quotient to 0 and restore the accumulator by adding divisor to it.
7. Then we reassemble the accumulator and quotient.
8. Decrement the count.
9. Repeat Step 2 to Step 8 until count equal to 0.
10. Return the quotient.

> Third Commit
# Running the code and testing the outputs
```
Dividing 10 by 3 yields: 3
Dividing 7 by -3 yields: -2
Dividing -2147483648 by 2147483647 yields: -1
Dividing 1981445587 by 1172010393 yields: 1
Dividing -2147483648 by -1 yields: 2147483648
Dividing 100579234 by -555806774 yields: -5
```
All of them are correct answers.

> Fourth Commit
# Creating dividetwointegers.py
Creating the dividetwointegers.py file to store the solution for 29. Divide Two Integers problem on LeetCode. Hurray. First proper github + leetcode colab by me.

> Fifth Commit
# Finding a more efficient solution
Instead of taking the unsigned restoring machine division algorithm approach, we will subtract the highest power of two's multiple of divisor from the dividend until the remainder is smaller than the divisor.

Approach:
1. Handle scope issue
2. Create variables a and b for dividend and divisor's absolute values respectively and also create a quotient variable.
3. store value of b in a temporary variable temp.
4. create a variable pwr with value 1.
5. Keep Left Shifting temp and pwr until a is not greater nor equal to the left shift of temp.
6. Subtract temp from a and add pwr to quotient.
7. Repeat Steps 3 to 6 while a >= b.
8. Return quotient if the sign of dividend and divisor is same and goto step 10.
9. Return -1 * quotient.
10. End.

> Sixth Commit
# Running optimized code

```
Dividing 10 by 3 yields: 3
Dividing 7 by -3 yields: -2
Dividing -2147483648 by 2147483647 yields: -1
Dividing 1981445587 by 1172010393 yields: 1
Dividing -2147483648 by -1 yields: 2147483648
Dividing 100579234 by -555806774 yields: -5
```
All of them are correct answers.

> Seventh Commit
# Creating dividetwointegers2.py for the optimized code and running it.
Creation and running was successful with improved time complexity.

> Eighth Commit
# Second Question:
Roman To Integer

Given a roman numeral, convert it to an integer.

> Ninth Commit
# Approach:
1. Initialize a map of Roman symbols to their integer values and set an accumulator num = 0.
2. Traverse the string from left to right.
3. If the current symbol is smaller than the next symbol, subtract its value from num.
4. Otherwise, add its value to num.
5. Repeat until all symbols are processed.
6. Return num.

> 10th Commit
# Running the code and testing the outputs
```
sol.romanToInt('CDLXXXVIII') yields: 488
sol.romanToInt('CDLXIX') yields: 469
sol.romanToInt('CDXLIX') yields: 449
```
All of them are correct answers.

> 11th Commit
# Creating romanToInt.py
Creating the romanToInt.py file to store the solution for 13. Roman to Integer problem on LeetCode and running the code.

> 12th Commit
# Third Question:
Remove Element Problem

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

> 13th Commit
# Approach:
1. Initialize a pointer t = 0 to track the position of the next valid element.
2. Traverse the array from left to right.
3. If the current element is not equal to val, copy it to index t and increment t.
4. Continue until all elements are processed.
5. Return t, the new length of the array without val.

> 14th Commit
# Running the code and testing the outputs and Creating removeElement.py
```
sol.removeElement([3,2,2,3], 3): 2
sol.removeElement([4, 5, 6, 7, 4, 4], 4): 3
sol.removeElement([11, 11, 11, 11], 11): 0
sol.removeElement([9, 7, 22, 7, 7, 3], 7): 3
```
All of them are correct answers.

Creating the removeElement.py file to store the solution for 27. Remove Element Problem on LeetCode and running the code.


> 15th Commit
# Fourth Question:
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

> 16th Commit
# Approach and running test cases:

1. Iterate through the haystack string from left to right.
2. At each index, check whether the current character matches the first character of needle.
3. If it matches, compare the substring starting at that index with needle.
4. If the substring matches, return the current index.
5. Continue this process until the end of haystack.
6. If needle is not found, return -1.

Test cases successfully passed.

>17th Commit
# Creating strStr.py and running it.
Creating the removeElement.py file to store the solution for 28. Find the Index of the First Occurrence in a String Problem on LeetCode and running the code.

Running the code successfully outputs:
```
0
-1
2
-1
```