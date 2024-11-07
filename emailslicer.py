# Email Slicer
# This email slicer slices the email into two parts. One for the username and second one for domain

email = input("Enter your email: ").strip() #Used strip incase there are any white spaces

# Use try except method to handle any potential errors

if "@" in email and email.count("@") == 1: # Validate if '@' is present in  email and if it is available only for once

    try:
        username = email[:email.index('@')] #Print the statement from 0 index to before the @
        domain = email[email.index('@') + 1: ] #Print the statement right after @ to the end
        print(f"Your username is {username} and domain is {domain}")
    except ValueError:
        print("Invalid email input")

else:
    print("Invalid email format. Make sure there is one '@' symbol.")
