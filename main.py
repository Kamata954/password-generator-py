#All the necessary imports for making this password program
import secrets
import string

#Defining all the possible characters that will make up a password with the string library
alphabet = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation

#Scan the password length from the user
pwd_length = int(
  input(
    "Hello User, welcome to Kimani’s secure password generator!\nBegin by entering the length of your desired password: "
  ))

#Start a loop that will determine whether numbers will be in the password or not, and prompt the user if they enter an invalid digit
while True:
  pwd_num = int(
    input(
      "\n\nWould you like your password to include numbers?\nPress 1 for yes and 2 for no: "
    ))
  if pwd_num == 1:
    comp_pwd = alphabet + numbers
    break
  elif pwd_num == 2:
    comp_pwd = alphabet
    break
  else:
    print("Sorry, that was an incorrect input.Try again")

#Start a loop that will determine whether special characters will be in the password or not, and prompt the user if they enter an invalid digit
while True:
  pwd_char = int(
    input(
      "\n\nWould you like your password to include special symbols? \nPress 1 for yes and 2 for no: "
    ))
  if pwd_char == 1:
    comp_pwd += special_chars
    break
  elif pwd_char == 2:
    break
  else:
    print("Sorry, that was an incorrect input. Try again")

#If both characters and numbers will be used, create a variable to use for an if statement to create a full password
full_pwd = 0
if pwd_num == 1 and pwd_char == 1:
  full_pwd = 1

#Password constraint using a loop for a full password that will include at least one number AND one special character
if full_pwd == 1:
  while True:
    password = ''
    for i in range(pwd_length):
      password += ''.join(secrets.choice(comp_pwd))
    if (any(char in numbers for char in password)
        and any(char in special_chars for char in password)):
      break

#Password constraint using a loop for a password that will include at least one number
elif pwd_num == 1:
  while True:
    password = ''
    for i in range(pwd_length):
      password += ''.join(secrets.choice(comp_pwd))
    if (any(char in numbers for char in password)):
      break

#Password constraint using a loop for a password that will include at least one special character
elif pwd_char == 1:
  while True:
    password = ''
    for i in range(pwd_length):
      password += ''.join(secrets.choice(comp_pwd))
    if (any(char in special_chars for char in password)):
      break

#Password with only letters from the alphabet will be generated
else:
  password = ''
  for i in range(pwd_length):
    password += ''.join(secrets.choice(comp_pwd))

#Print out the generated password
print("Password generation complete!\nYour generated secure password is: " +
      password)
