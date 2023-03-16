"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
"""
#user_names = ['sam', 'mike', 'admin', 'fred']
user_names = []
if user_names:    
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello", user_name, "would you like to see a status report?")
        else:
            print("Hello", user_name.title(), "it's nice to see you again!")
else:
    print("We need to find us some users fast!")                