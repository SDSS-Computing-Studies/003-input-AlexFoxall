#! python3
"""
Ask the user for their name and their email address.
You will need to use the .strip() method for this assignment. Be aware of your 
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.
"""
#input name 
question = input("what is your name?")
question = question.strip()
question2 = input("what is your email?")
question2 = question2.strip()
print("Your name is " + question +"," " and your email is " + question2)
