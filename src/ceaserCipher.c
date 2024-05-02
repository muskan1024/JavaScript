#include <stdio.h>
void caesarEncrypt(char message[], int shift);
void caesarDecrypt(char message[], int shift);
int main() {
 char message[100];
 int shift;
 // Get input
 printf("Enter a message: ");
 fgets(message, sizeof(message), stdin);
 printf("Enter the shift value: ");
 scanf("%d", &shift);
 // Encryption
 printf("\nEncrypted Message: ");
 caesarEncrypt(message, shift);
 // Decryption
 printf("\nDecrypted Message: ");
 caesarDecrypt(message, shift);
 return 0;
}
void caesarEncrypt(char message[], int shift) {
 int i;
 for (i = 0; message[i] != '\0'; i++) {
 // Encrypt only alphabets
 if (message[i] >= 'A' && message[i] <= 'Z') {
 message[i] = ((message[i] - 'A' + shift) % 26) + 'A';
 } else if (message[i] >= 'a' && message[i] <= 'z') {
 message[i] = ((message[i] - 'a' + shift) % 26) + 'a';
 }
 printf("%c", message[i]);
 }
}
void caesarDecrypt(char message[], int shift) {
 int i;
 for (i = 0; message[i] != '\0'; i++) {
 // Decrypt only alphabets
 if (message[i] >= 'A' && message[i] <= 'Z') {
 message[i] = ((message[i] - 'A' - shift + 26) % 26) + 'A';
 } else if (message[i] >= 'a' && message[i] <= 'z') {
 message[i] = ((message[i] - 'a' - shift + 26) % 26) + 'a';
 }
 printf("%c", message[i]);
 }
}


// Algorithm:  
// Here's a simple algorithm for the Caesar Cipher:  
  
// a. Encryption:  
// -	Read the plaintext message and the shift value.  
// -	For each character in the plaintext:  
// -	If it is a letter, shift it by the specified value.  
// -	If it is not a letter, leave it unchanged.  
// -	Print the encrypted message.  
  
// b. Decryption:  
// -	Read the encrypted message and the shift value.  
// -	For each character in the encrypted message:  
// -	If it is a letter, shift it backward by the specified value.  
// -	If it is not a letter, leave it unchanged.  
// -	Print the decrypted message.  
