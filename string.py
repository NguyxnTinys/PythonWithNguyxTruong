course = "Python for beginners"
num = 1234
print(course.upper()) #using uppercase string
print(course.lower()) #using lower string

#[1] find
#course.find('x') return first index if x appears in course else not found return -1
# x could be a character or a sequuence of characters 

# Example:course = 'Python for Beginner'
# Index:            0123456789...
print(course.find('Python'))  # res = 0
print(course.find('for'))  # res = 7
print(course.find('y'))  # res = 1
print(course.find('Y'))  # res = -1

#[2] replace
print(course.replace('for', '4'))
# print(num.replace(1234, 3)) Bug: 'int' object has no attribute 'replace'

#[3] in
print('Python' in course) # res = True
