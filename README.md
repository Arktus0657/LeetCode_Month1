>Initializing Commit
# LeetCode_Month1.ipynb Creation
This is the first month of uploading my leetcode practicing to github in a ipynb style

>First Commit
### First Question:
Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

>Second Commit

Approach: 
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

>Third Commit

Running the code and testing the outputs

>Fourth Commit
# Creating dividetwointegers.py
Creating the dividetwointegers.py file to store the solution for 29. Divide Two Integers problem on LeetCode. Hurray. First proper github + leetcode colab by me.

>Fifth Commit
# Finding a more efficient solution
Instead of taking the unsigned restoring machine division algorithm approach, we will subtract the highest power of two's multiple of divisor from the dividend until the remainder is smaller than the divisor.

Aproach:
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