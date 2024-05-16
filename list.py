numbers = [1,2,3,4,5,6]
print ('Original: ', numbers)

first_element = numbers[0]
print ('First number: ', first_element)

last_element = numbers[5]
print ('Last number: ', last_element)

subset = numbers[2:4]
print ('Subset: ', subset)

numbers [3] = 8
print ('Modified: ', numbers)

numbers.append(8)
print ('New list after add 8 to the end:', numbers)

numbers.remove(2)
print (':ist after removing 2: ', numbers)

index_of_6 = numbers.index(6)
print ('Index of 6: ', index_of_6)

contains_4 = 4 in numbers
print ('Does the list contain 4: ', contains_4)

numbers.sort()
print ('Sort list: ', numbers)

numbers.reverse()
print ('Reversed list: ', numbers)

animals = ['dogs', 'cats', 'bird']
print (animals)
print (animals[0])