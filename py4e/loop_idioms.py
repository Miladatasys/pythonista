zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15 ]:
    zork = zork + thing
    print(zork,thing)
print('After', zork)

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + value
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3:
        print(found, value)
print('After', found)

# There's a variable called NONE Type and it has one constant in it
# Flat Value
# The "is" and "is not" are operators
smallest_so_far = None
print('Before', smallest_so_far)
for value in [ 9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far:
        print(smallest_so_far, value)
print('After', smallest_so_far)

n = 5
while n > 0:
    print(n)
    n -= 1
print("All done")

n = 5
while n > 0 :
    print(n)
    if n == 3:
        break
    n -= 1
print("All done")

n = 5
while n > 0 :
    n -= 1
    if n == 3:
        continue
    print(n)
print("Loop ended")

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

friends = ['Joseph', 'Glen', 'Sally']
for friend in friends:
    print("Happy new Year:", friend)
print("Done!")

zork = 0
for thing in [ 9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

smallest_so_far = -1
for the_num in  [9, 41, 12, 3, 74, 15] :
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far)