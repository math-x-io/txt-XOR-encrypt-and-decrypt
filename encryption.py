from functions import dec2bin, text2bin, bin2text, encrypt_xor

file = input("which .txt file do you want to encrypt ? : ")
print()
f = open(file,'r')
msg = f.read()
print("encrypted message : "+msg)
f.close()
print()

key_int = input("enter a integer number for your key : ")
print()
key = dec2bin(int(key_int))

file_binary=text2bin(msg)
file_crypt=bin2text(encrypt_xor(file_binary,key))
nameEncryptFile= file.replace(".txt","")+"_XOR_Encrypted.txt"

f2 = open(nameEncryptFile, "w") 
f2.write(file_crypt) 
f2.close()


print("successful file XOR encryption !")