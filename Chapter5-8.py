"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
in again.
"""
user_names = ['j_sparrow', 'admin', 'm_gillis', 't_orlando']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello", user_name, "would you like to see a status report?")
    else:
        print("Hello", user_name, "it's nice to see you again!")    