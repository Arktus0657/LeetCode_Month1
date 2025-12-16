>Initializing Commit
# LeetCode_Month1.ipynb Creation
This is the first month of uploading my leetcode practicing to github in a ipynb style

>First Commit
# First Question:
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
#Running the code and testing the outputs
```
Dividing 10 by 3 yields: 3
Dividing 7 by -3 yields: -2
Dividing -2147483648 by 2147483647 yields: -1
Dividing 1981445587 by 1172010393 yields: 1
Dividing -2147483648 by -1 yields: 2147483648
Dividing 100579234 by -555806774 yields: -5
```
All of them are correct answers.

>Fourth Commit
# Creating dividetwointegers.py
Creating the dividetwointegers.py file to store the solution for 29. Divide Two Integers problem on LeetCode. Hurray. First proper github + leetcode colab by me.

>Fifth Commit
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

>Sixth Commit
#Running optimized code

```
Dividing 10 by 3 yields: 3
Dividing 7 by -3 yields: -2
Dividing -2147483648 by 2147483647 yields: -1
Dividing 1981445587 by 1172010393 yields: 1
Dividing -2147483648 by -1 yields: 2147483648
Dividing 100579234 by -555806774 yields: -5
```
All of them are correct answers.

>Seventh Commit
#Creating dividetwointegers2.py for the optimized code and running it.
Creation and running was successful with improved time complexity.

>Eighth Commit
# Second Question:
Roman To Integer
Given a roman numeral, convert it to an integer.

>Ninth Commit

Approach:
1. Initialize a map of Roman symbols to their integer values and set an accumulator num = 0.
2. Traverse the string from left to right.
3. If the current symbol is smaller than the next symbol, subtract its value from num.
4. Otherwise, add its value to num.
5. Repeat until all symbols are processed.
6. Return num.

> 10th Commit
#Running the code and testing the outputs
```
sol.romanToInt('CDLXXXVIII') yields: 488
sol.romanToInt('CDLXIX') yields: 469
sol.romanToInt('CDXLIX') yields: 449
```
All of them are correct answers.

>11th Commit
# Creating romanToInt.py
Creating the romanToInt.py file to store the solution for 13. Roman to Integer problem on LeetCode and running the code.