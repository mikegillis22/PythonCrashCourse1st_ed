"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
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
print(f"Hello {dinner_list[2].title()} you're invited to dinner next Friday.")