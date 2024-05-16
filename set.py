fruits = {'apple', 'orange', 'mango'}
fruits.add("grape")
print (fruits)

fruits.remove ('apple')
print (fruits)

contains_banana = 'banana' in fruits
print ('Does \'banana\' in fruits: ', contains_banana)

contains_mango = 'mango' in fruits
print ('Does \'mango\' in fruits: ', contains_mango)

print ('Fruits:')
for fruit in fruits:
    print (fruit)

add_fruits = {'lime', 'watermelon', 'orange'}

#combine all but not duplicate
union_all_fruits = fruits.union(add_fruits)
print (union_all_fruits)

#only display same element from two sets
intersection_fruits = fruits.intersection(add_fruits)
print (intersection_fruits)

#display not same element from set fruits
difference_fruits = fruits.difference(add_fruits)
print (difference_fruits)
#display not same element from set add_fruits
print (add_fruits.difference(fruits))