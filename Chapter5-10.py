"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
"""
current_users = ['sam', 'mike', 'admin', 'fred', 'mark']
print(current_users)
new_users = ['peter', 'MIKE', 'Mike', 'scott', 'brad', 'sam']
for user_name in new_users:
        if user_name.lower() in current_users:
            print("The user name", user_name, "is not available. Please select another.")
        else:
            print("The user name", user_name, "is available. ")
            current_users.append(user_name.lower())
print(current_users)
          