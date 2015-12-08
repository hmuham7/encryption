import fileinput

act_file = raw_input("Please Enter the name of the text file to be encypted: ")
enc_file = raw_input("Please Enter the name of a file to store the encrypted message: ")
key = raw_input("Enter the key to encrypt the message: ")

f_in = open(act_file, 'r+')
f_out = open(enc_file, 'w')

f_in.close()
f_out.close()

