# file operations

# open
# with open
'''
file = open('home.txt', 'r')
for i in file:
	print(i)
#print(file.read())
'''
'''
file = open('home.txt', 'w')
file.write('Hi! Karti....')
file.close()
'''
'''
file = open('home.txt', 'a')
file.write('Hi! Karti....')
file.close()
'''
'''
with open('home.txt', 'r') as file:
	for line in file.readlines():
		print(line.split()[1])

'''
'''
file = open('home.txt', 'r')
print(file.read())
file.close()
'''
'''
file = open('home.txt', 'w')
file.write('Hello All...')
file.close()
'''
'''
file = open('home.txt', 'a')
file.write('105 Ram Ibm 36000')
file.close()
'''

with open('home.txt', 'r') as f:
	print(f.read().strip(''))









