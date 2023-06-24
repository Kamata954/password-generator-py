# Secure Python Password Generator
A simple password generator that makes highly secure passwords using python. Prompts the user for the length of desired password and complexity.

**Link to project:** https://replit.com/@KimaniWalker/secure-password-generator#

![alt tag](https://i.imgur.com/n0irj7s.png)

## How It's Made:

**Tech used:** Python

The key to making this password generator secure is by using the secrets module. The secrets module provides cryptographically strong and random passwords, much more secure than the random module.

The program prompts the user to enter the length of their desired password, as well as asking them whether they wish to have numbers in their password and symbols. The program then generates a password, that will include numbers and/or special characters if the user prompted the program to do so, and outputs the generated password.


## Lessons Learned:

Going into this project, my first instinct was to use to random module to generate random characters, but upon further research, I found that the random module isn't truely random and is not secure when it comes to password generation. That's when I learned about the secrets module when looking for a more secure alternative to random.

I also could optimize the code by putting in chunks of the codes in functions and doing function calls.






