"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.
"""
OddNumbers = []
for odd in range(1,21,3):
    OddNumbers.append(odd)
    print(odd)