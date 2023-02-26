"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
"""
threes = []
for three in range(3,31):
    threes.append(three*3)
    print(max(threes))
print(threes)    