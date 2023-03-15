"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""
car = 'Rambler'
print("Is car == 'Rambler'?")
print(car.lower() == 'rambler')
print("\nIs car == 'Ranger'?")
print(car.lower() == 'ranger')
print()

favFruit = ['blueberries', 'raspberries', 'blackberries', 'cherries', 'strawberries']
for fruit in favFruit:
    print(fruit.title())
print('bananas' in favFruit)
print('cherries' in favFruit)
fruit = 'bananas'
if fruit not in favFruit:
    print("Yes! We have no", fruit.title(), "we have no", fruit.title(), "today.")
print() 
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())