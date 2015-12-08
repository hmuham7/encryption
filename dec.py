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

# closing the files after performing operations
f_in.close()
f_out.close()

