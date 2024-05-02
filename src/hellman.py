def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def diffie_hellman(p, g, x, y):
    # Calculate public keys
    A = mod_exp(g, x, p)
    B = mod_exp(g, y, p)
    # Calculate shared keys
    key1 = mod_exp(B, x, p)
    key2 = mod_exp(A, y, p)
    return key1, key2

# User input for n and g
p = int(input("Enter the value of p: "))
g = int(input("Enter the value of g: "))

# User input for private keys
x = int(input("Enter the private key a for Alice: "))
y = int(input("Enter the private key b for Bob: "))

# Perform Diffie-Hellman key exchange
key1, key2 = diffie_hellman(p, g, x, y)

print("Secret key for the Alice is:", key1)
print("Secret key for the Bob is:", key2)


# Diffie-Hellman algorithm:
# The Diffie-Hellman algorithm is being used to establish a shared secret that can be used for secret communications while exchanging data over a public network using the elliptic curve to generate points and get the secret key using the parameters.
    # •	For now, we will consider only 4 variables, one prime P and G (a primitive root of P) and two private values a and b.
    # •	P and G are both publicly available numbers. Users (say Alice and Bob) pick private values a and b and they generate a key and exchange it publicly. The opposite person receives the key and that generates a secret key, after which they have the same secret key to encrypt.

# Step 1: Alice and Bob get public numbers P = 23, G = 9
# Step 2: Alice selected a private key a = 4 and 
#         Bob selected a private key b = 3
# Step 3: Alice and Bob compute public values 
#         Alice:	x =(9^4 mod 23) = (6561 mod 23) = 6
#         Bob:	y = (9^3 mod 23) = (729 mod 23) = 16
# Step 4: Alice and Bob exchange public numbers 
# Step 5: Alice receives public key y =16 and
#         Bob receives public key x = 6
    
# Step 6: Alice and Bob compute symmetric keys 
#         Alice: ka = y^a mod p = 65536 mod 23 = 9 
#         Bob:	kb = x^b mod p = 216 mod 23 = 9

# Step 7: 9 is the shared secret.
