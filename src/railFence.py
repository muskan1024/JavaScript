# Railfence Cipher
def Railfence(key, textsize):
    counter = 0
    sign = "+"
    railfence = ""

    for i in range(textsize):
        counter = eval(f"{counter}{sign}1")
        railfence+=str(counter)
        if counter==key:
            sign='-'
        elif counter==1:
            sign='+'
    #print(railfence)
    return railfence

def encrypt(plaintext,key):
    textsize = len(plaintext)
    ciphertext = ""
    railfence = Railfence(key=key,textsize=textsize)

    for i in range(1,key+1):
        for char_i in range(textsize):
            if railfence[char_i]==f"{i}":
                ciphertext=ciphertext+plaintext[char_i]
    return ciphertext

def decrypt(ciphertext,key):
    textsize = len(ciphertext)
    plaintext = ""
    railfence = Railfence(key=key,textsize=textsize)

    antirailfence = sorted([index for index in railfence])
    #print(antirailfence)

    for char_i in range(textsize):
        for j in range(textsize):
            if railfence[char_i]==antirailfence[j]:
                ch = ciphertext[j]
                antirailfence[j]=0
                break
        plaintext+=ch
    return plaintext
    

plaintext = input("Enter a Plaintext: ")
key = int(input("Enter Key: "))

ciphertext = encrypt(plaintext=plaintext,key=key)

print(ciphertext)

print(decrypt(ciphertext=ciphertext,key=key))


# Algorithm: 
  
# Encryption Algorithm:  
# Step 1:  Input the plaintext and the number of rails.  
# Step 2:  Create a matrix with the number of rows equal to the number of rails.  
# Step 3:  Fill in the matrix by placing each character of the plaintext in a zigzag pattern.  
# Step 4:  Read the characters from the matrix row-wise to get the ciphertext.  
 
# Decryption Algorithm:  
# Step 1:  Input the ciphertext and the number of rails.  
# Step 2:  Create a matrix with the number of rows equal to the number of rails.  
# Step 3:  Fill in the matrix by placing each character of the ciphertext in a zigzag pattern.  
# Step 4:  Read the characters from the matrix in the order they were written to get the original plaintext.  
