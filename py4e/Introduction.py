# Variable names in Python must start with a letter (a-z, A-Z) or an underscore (_).
# Python is case-sensitive, so 'myVariable' and 'myvariable' are different variables.
# It's generally recommended to avoid starting variable names with an underscore unless it's for special use (e.g., private variables).
x = 1
print(x)


x = x + 1
print(x)

# Reserved Words (A reminder that they are predefined and can't be used as variable names)
# [False, True, None, if, else, for, while, etc.]

# Sequential Steps
x = 2
print(x)

x = x + 2
print(x)

# Conditionals
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

# Repeated Steps - Loops
n = 5
while n > 0:
    print(n)
    n = n - 1  # Decrease n by 1
print('Blastoff!')

# Constants 
# could be numeric and string that uses singles quotes (') or double quotes("") a variable does change

# Variable (mutable)
total_price = 200
total_price = total_price * 1.1  # Value changes based on a calculation

# Constant (immutable, by convention)
TAX_RATE = 0.07  # This value should not change throughout the program

# Numeric Expressions
xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

# The modulo operator (%) returns the remainder of a division. Here, we divide 23 by 5.
# The result is the remainder of 23 / 5, which is 3.
jj = 23
kk = jj % 5 # Modular expression
print(kk)

# Exponentiation
print(4 ** 3)

# Order of Evaluation
# Order of Evaluation (Operator Precedence)
# Python follows the PEMDAS rule for evaluating expressions:
# 1. Parentheses () are evaluated first.
# 2. Exponents (**) or Power come next.
# 3. Multiplication (*) and Division (/) are evaluated from left to right.
# 4. Addition (+) and Subtraction (-) are evaluated last, also from left to right.
# This expression will be evaluated step by step based on these rules.

x = 1 + (2 * 3) - (4 / (5 ** 6)) # First calculate 5**6, then the division, multiplication, addition, and subtraction
print(x)

# Type matters type()
# You can also use int() and float() to convert between strings and integers

# User Input
nam = input('Who are you?')
print('Welcome', nam)
