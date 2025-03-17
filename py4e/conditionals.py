# Comparison Operators
x = 5
if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')

if x < 6: print('Less than 6')
if x <= 5:
    print('Less or Equals 5')
if x != 6:
    print('Not equal 6')

# Nested Decisions
x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

# Two-way Decisions with else:
x = 4
if x > 2:
    print('Bigger')
else:
    print('All done')

# Multi-way
x = 5
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print("All done")

# Try and Except
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')

