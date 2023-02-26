"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
"""
#cubes = []
#for cubed in range(1,11):
    #cubes.append(cubed**3)
    #print(max(cubes))
#print(cubes)

cubes = [cubed**3 for cubed in range(1,11)]
print(cubes) 