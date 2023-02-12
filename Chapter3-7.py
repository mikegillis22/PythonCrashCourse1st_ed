"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
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
print(f"Hello {dinner_list[5].title()} you're invited to dinner next Friday.\n")
print("Sadly, we will be unable to accommodate the number of guests that we had hoped to.\n")
#print(dinner_list)
popped_dinner_guest = dinner_list.pop()
print(f"We're so sorry {popped_dinner_guest.title()}, we are unable to invite you to dinner this Friday.")
popped_dinner_guest = dinner_list.pop()
print(f"We're so sorry {popped_dinner_guest.title()}, we are unable to invite you to dinner this Friday.")
popped_dinner_guest = dinner_list.pop()
print(f"We're so sorry {popped_dinner_guest.title()}, we are unable to invite you to dinner this Friday.")
popped_dinner_guest = dinner_list.pop()
print(f"We're so sorry {popped_dinner_guest.title()}, we are unable to invite you to dinner this Friday.\n")
print(f"Hello {dinner_list[0].title()} you're still invited to dinner next Friday.")
print(f"Hello {dinner_list[1].title()} you're still invited to dinner next Friday.")
del dinner_list[1]
del dinner_list[0]
print(dinner_list)