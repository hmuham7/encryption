#########################################
#  ECE 2524: Intro to Unix      	#
#  Project #3: Python and Git   	#
# 					#
#  Submitted By: Muhammad Hassan	#
#  Date Created: 12/08/15		#
#					#
#  enc.py				#
#########################################

import fileinput

# Reading the raw input from user to get the plain-text message file name, key and a filename to store encrypted message
# User is supposed to enter a key in hexadecimal format for the algorithm to work.
act_file = raw_input("Please Enter the name of the text file to be encypted: ")
enc_file = raw_input("Please Enter the name of a file to store the encrypted message: ")
key = raw_input("Enter the key to encrypt the message: ")

# opening the files for read and write
f_in = open(act_file, 'r+')
f_out = open(enc_file, 'w')


# closing the files after performing operations
f_in.close()
f_out.close()

