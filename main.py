#This is my file, it has a function that removes valuse and an RLE compression algorithm
def rmVowel(arg):
	return arg.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
def compress(arg):
	temp = ""
	x = "a"
	ind = 0
	xInt = 0
	for i in arg:
		if(ind==0):
			ind += 1
			x = i
		if(i==x):
				xInt += 1
		else:
			temp += x + str(xInt)
			xInt = 1
			x=i
	temp += x + str(xInt)
	return temp

myStr = raw_input()
myStr = compress(myStr)
print(myStr)
