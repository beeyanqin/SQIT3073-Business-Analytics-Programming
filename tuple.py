animals = ('dogs', 'cats', 'birds', 'rabbits', 'monkeys', 'cows')

first_animals = animals[0]
print ('First animal: ', first_animals)
last_animals = animals[0]
print ('Last animal: ', last_animals)

print ("Animals: ")
for animal in animals:
    print(animal)

contains_birds = 'birds' in animals
print ('Does \'bird\' in tuple: ', contains_birds)

contains_ants = 'ants' in animals
print (' Does \'ants\' in animals: ', contains_ants)

print (len(animals))

more_animals = ('chicken', 'duck')
all_animals = more_animals + animals
print (all_animals)

nested_tuple = ('red', ('blue', 'yellow'))
print (nested_tuple)