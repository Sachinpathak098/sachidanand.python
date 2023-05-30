# string to search in file
with open(r'myfile.txt', 'r') as fp:
	# read all lines using readline()
	lines = fp.readlines()
	for row in lines:
		# check if string present on a current line
		word = 'Line 3'
		#print(row.find(word))
		# find() method returns -1 if the value is not found,
		# if found it returns index of the first occurrence of the substring
		if row.find(word) != -1:
			print('string exists in file')
			print('line Number:', lines.index(row))