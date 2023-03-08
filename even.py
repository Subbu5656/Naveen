l = [1,2,3,4,5,6,7,8]
def even(l):
	output = [i for i in l if i%2==0]
	return output
print(even(l))