'''
Account Login
'''
#Login details
details = ["bankole", "victor","ezekiel", "praise", "morolayo", "toluwanimi"]
#Create a new list from the old one so as to ensure victor is no longer a part of the list
new_list = [x for x in details if x != "victor"]
#Output begins
print("Hello there")
user_input = input("Enter your username")
# Using the if prompt to check if the name is in the new list
if user_input in new_list:
    print("Welcome!")
else:
    print("Unauthorised User")
