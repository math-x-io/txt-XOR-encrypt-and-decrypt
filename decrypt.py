from functions import dec2bin, text2bin, bin2text, encrypt_xor


file = input("which .txt file do you want to decrypt ? : ")
print()
f = open(file,'r')
msg = f.read()
print("message to decrypt : "+msg)
f.close()
print()

msg_binary = text2bin(msg)

key_int = input("enter the key : ")
key = dec2bin(int(key_int))

decrypt = encrypt_xor(msg_binary, key)
nameDecryptFile= file.replace(".txt","")+"_Decrypted.txt"
f2 = open(nameDecryptFile, "w") 
f2.write(bin2text(decrypt)) 
f2.close()
print("Successful file decryption !")