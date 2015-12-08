import fileinput

enc_file = raw_input("Please Enter the name of the file to be decrypted: ")
ret_file = raw_input("Please Enter the name of a file to store the decrypted message: ")
key = raw_input("Enter the key to decypt the message: ")

f_in = open(enc_file, 'r+')
f_out = open(ret_file, 'w')

f_in.close()
f_out.close()

