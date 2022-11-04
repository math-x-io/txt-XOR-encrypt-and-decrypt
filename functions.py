# Library of functions for manipulate int & binary number and encrypt on XOR a binary number 

#function for convert decimal to binary on String format
def dec2bin(n):
    s = ""
    if n==0:
        return "00000000"
    while n>0:
        n, r = n//2,n%2
        s=str(r)+s
        
    s=s.zfill(8)
    return s

#function for convert a text to binary on String format
def text2bin(txt):
    chain=""
    for l in txt:
        b=ord(l)
        chain+=dec2bin(b)
    return chain

#function for convert a binary to text 
def bin2text(binary):
    chain=""
    for b in range(0,len(binary),8):
        a=chr(int(binary[b:b+8],2))
        chain+=a
    return chain

#function for encrypt a binary with key on a XOR encrypt
def encrypt_xor(binary,key):
    chain=""
    for b in range(0,len(binary)): 
        a=int(binary[b])^int(key[b%len(key)])
        chain+=str(a)
    return chain