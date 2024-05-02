def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryption(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 

def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

if __name__ == "__main__": 
  string = input("Enter the message: ")
  keyword = input("Enter the keyword: ")
  key = generateKey(string, keyword) 
  encrypt_text = encryption(string,key) 
  print("Encrypted message:", encrypt_text) 
  print("Decrypted message:", decryption(encrypt_text, key))
  
  
# Algorithm: -
# Encryption:
# Step 1) Choose a keyword or phrase that both the sender and receiver know (e.g., "KEY").
# Step 2) Repeat the keyword or phrase to match the length of the plaintext message (e.g., "KEYKEYKEY").
# Step 3) Align the keyword above the plaintext.
# Step 4) Convert each letter of the keyword and plaintext to a numerical value (e.g., A=0, B=1, C=2, etc.).
# Step 5) Add the numerical values of the corresponding letters in the keyword and plaintext.
# Step 6) Take the result modulo 26 (as there are 26 letters in the alphabet).
# Step 7) Convert the resulting numbers back to letters using the same numerical mapping (A=0, B=1, C=2, etc.).

# Decryption:
# Step 1) Repeat the received keyword or phrase to match the length of the ciphertext message (e.g., "KEYKEYKEY").
# Step 2) Align the keyword above the ciphertext.
# Step 3) Convert each letter of the keyword and ciphertext to a numerical value (e.g., A=0, B=1, C=2, etc.).
# Step 4) Subtract the corresponding numeric value of keyword letter from ciphertext letter.
# Step 5) Add 26 if the result is negative.
# Step 6) Convert the resulting numbers back to letters using the same numerical mapping (A=0, B=1, C=2, etc.).
