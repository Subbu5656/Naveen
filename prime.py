'''
n = 13#int(input('Please enter a number:'))
try:
	if n>1 and not str:
		for i in range(2, int(n/2)+1):
			if n%i == 0:
				print('The given number is not a Prime:', n)
				break
		else:
			print('The given number is Prime:', n)
	else:
		print('The given number is not a Prime:', n)
except:
	print('It will accept Intergers only')
'''
xml_string="""<?xml version="1.0" encoding="UTF-8"?> <note> <to>Tove</to> <from>Jani</from> <heading>Reminder</heading> <body></body> </note> """


print(' '.join([i.replace('<body></body>','hello python') for i in xml_string.split()[3:]]))


