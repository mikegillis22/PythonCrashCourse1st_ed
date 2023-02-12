"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

dinner_list= ['chuck norris', 'harry aziz', 'joe campisi']
print(f"Hello {dinner_list[0].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[1].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[2].title()} you're invited to dinner next Friday.\n")
popped_dinner_guest = dinner_list.pop()
print(f"It looks like {popped_dinner_guest.title()} will not be able to make it to dinner on Friday.\n")
dinner_list.append('jack sparrow')
print(f"Hello {dinner_list[0].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[1].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[2].title()} you're invited to dinner next Friday.\n")
print("We have located a larger dinner table so as to accommodate additional guests.\n")
dinner_list.insert(0,'bruce lee')
dinner_list.insert(2,'jason bourne')
dinner_list.append('mr. spock')
print(f"Hello {dinner_list[0].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[1].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[2].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[3].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[4].title()} you're invited to dinner next Friday.")
print(f"Hello {dinner_list[5].title()} you're invited to dinner next Friday.")