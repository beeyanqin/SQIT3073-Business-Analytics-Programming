student = {'Name':'Lim',
           'Age' : 21,
           'Major' : 'Decision Science',
           'Grade' : {'Math' : 'A',
                      'Science' : 'A',
                      'BM' : 'A',
                      'BI' : 'A',
                      'BC' : 'A',
                      'Add Math' : 'A'}
            }
student_name = student ["Name"]
print ('Student name: ', student_name)
student_age = student ['Age']
print ('Student age: ', student_age)
student_major = student ['Major']
print ('Student major: ', student_major)
student_grade = student ['Grade']
print ('Grade: ', student_grade)
print ('Grade on Math: ', student ['Grade']['Math'])

student ['Age'] = 20
student ['Grade']['Math'] = 'A+'
print ('Updated age: ', student ['Age'])
print ('Updated Math grade: ', student ['Grade']['Math'])

student ['Gender'] = 'Female'
print ('Student gender: ', student ['Gender'])

print (student)

contains_major = 'Major' in student
print (contains_major)
contains_height = 'Height' in student
print (contains_height)

student_keys = student.keys()
print (student_keys)
student_values = student.values()
print (student_values)

print ('Student information:')
for key, value in student.items():
    print (f'{key} : {value}')

del (student['Grade'])
print (student)
print ("Student information after removing \'grade\':")
for key, value in student.items():
    print (f"{key} : {value}")