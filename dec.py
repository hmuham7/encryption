#########################################
#  ECE 2524: Intro to Unix      	#
#  Project #3: Python and Git   	#
# 					#
#  Submitted By: Muhammad Hassan	#
#  Date Created: 12/08/15		#
#					#
#  dec.py				#
#########################################

import fileinput

# Reading the raw input from user to get the encypted message file name, key and a filename to store retreived message
enc_file = raw_input("Please Enter the name of the file to be decrypted: ")
ret_file = raw_input("Please Enter the name of a file to store the decrypted message: ")
key = raw_input("Enter the key to decypt the message: ")

# opening the files for read and write
f_in = open(enc_file, 'r+')
f_out = open(ret_file, 'w')

# for loop to read all the lines in text file and perform ecnryption
for line in f_in:
	string = line
	newkeystring = ''
	hexstring = string.encode("hex") # converting the text into hexa-decimal format
	keystring = key.decode("hex")

	# inner for loop to extend the key to upto the length to string (line size) as that key will be used late to XOR, so the length
	# has to be a match
	for i in range(0,len(string)):
    		newkeystring+=keystring[i%len(keystring)]
	
	newkey = newkeystring.encode("hex") # encoding the newly resized key to hexadecimal
	decipherstring = int(hexstring, 16) ^ int(newkey, 16) # performing XOR operation
	decipher = '{:x}'.format(decipherstring)
	decipher_str = decipher.decode("hex")
	f_out.write(decipher_str) # storing the XOR-ed string into a text file (or otherwise called retreived message)

# closing the files after performing operations
f_in.close()
f_out.close()

