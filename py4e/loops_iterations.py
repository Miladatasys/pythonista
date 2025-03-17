n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)