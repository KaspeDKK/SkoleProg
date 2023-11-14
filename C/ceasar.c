#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * Encrypts the given text using the Caesar cipher.
 *
 * The Caesar cipher shifts each letter in the text by a number of places
 * specified by the key. Only alphabetic characters are encrypted; other
 * characters remain unchanged.
 *
 * @param text The text to encrypt (modified in place).
 * @param key  The number of positions to shift each letter.
 */
void caesar_encrypt(char *text, int key) {
    // Loop through each character of the text
    for (int i = 0; i < strlen(text); i++) {
        char ch = text[i];

        // If the character is an uppercase letter, shift it by 'key' positions
        if (ch >= 'A' && ch <= 'Z') {
            ch = (ch - 'A' + key) % 26 + 'A';
        }
        // If the character is a lowercase letter, shift it by 'key' positions
        else if (ch >= 'a' && ch <= 'z') {
            ch = (ch - 'a' + key) % 26 + 'a';
        }

        // Update the text with the encrypted character
        text[i] = ch;
    }

    // Display the encrypted text
    printf("Encrypted text: %s\n", text);
}

/**
 * Entry point of the program.
 * 
 * Takes in command line arguments: the text to be encrypted and the Caesar key.
 * The program then calls the caesar_encrypt function to perform the encryption.
 */
int main(int argc, char *argv[]) {
    // Check for correct number of command line arguments
    if (argc != 3) {
        printf("Usage: ./caesar <text> <key>\n");
        return 1; // Error return
    }

    // Extract text and key from command line arguments
    char *text = argv[1];
    int key = atoi(argv[2]);  // Convert key from string to integer

    // Call the encryption function
    caesar_encrypt(text, key);
    return 0; // Succes return
}
