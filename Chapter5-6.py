"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder.
"""
name = input("What is your name? ")
age = input("What is your age? ")
if (float(age) < 2) and (float(age) > 0):
    print("Hello", name, "you're just a baby.")
elif (int(age) >= 2) and (int(age) < 4):
    print("Hello", name, "you're just a toddler.")
elif (int(age) >= 4) and (int(age) < 13):
    print("Hello", name, "you're a kid.")
elif (int(age) >= 13) and (int(age) < 20):
    print("Hello", name, "you're a teenager.")
elif (int(age) >= 20) and (int(age) < 65):
    print("Hello", name, "you're an adult.")
elif (int(age) >= 65) and (int(age) <= 125):
    print("Hello", name, "you're an elder.")
elif (int(age) > 125):
    print ("Hello", name, "you're either an alien, a time traveler, or a vampire.")
else:
    print("Please enter an age that is greater than zero.")    