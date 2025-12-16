>Initializing Commit
# LeetCode_Month1
This is the first month of uploading my leetcode practicing to github in a ipynb style

>First Commit
### First Question:
Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

>Second Commit
Approach: 
1. We are using the classic restoring division algorithm but summing the accumulator to the dividend(quotient) and assign the count as length of dividend.
2. We Shift left the sum of accumulator and quotient. 
3. Then after splitting them back. 
4. We subtract the accumulator by the divisor.
5. If the sign of the divisor is positive then we assign the last bit of quotient to 1.
6. If the sign of the divisor is negative then we assign the last bit of quotient to 0 and restore the accumulator by adding divisor to it.
7. Then we reassemble the accumulator and quotient.
8. Decrement the count.
9. Repeat Step 2 to Step 8 until count equal to 0.
10. Return the quotient.

>Third Commit
Running the code and testing the outputs