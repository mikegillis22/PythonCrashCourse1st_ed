"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""
fruit_basket = ['apples', 'oranges', 'plums', 'peaches', 'grapes', 'bananas', 
                'blueberries', 'raspberries', 'blackberries', 'strawberries']
check_basket = input("Let's check your fruit basket for? ")
if check_basket in fruit_basket:
    print("Yes!", check_basket, "are in your basket.")
else:
    print("No, there are no", check_basket, "in your basket")    