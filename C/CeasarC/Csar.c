#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "headers.h"

/**
 * File: Csar.c 
 * Author: KaspeDKK - <https://github.com/kaspedkk>
 * 
 * Description: Applies the Caesar cipher to a given string.
 * 
 * @param text The string to be encrypted or decrypted.
 * @param key The number of positions that each character in the text is shifted.
 * @param encrypt A flag to indicate whether to encrypt (1) or decrypt (0).
 * 
 */
void caesar_cipher(char *text, int key, int encrypt) {
    int length = strlen(text); // Calculate the length of the string once
    for (int i = 0; i < length; i++) {
        // Determine the direction of the shift based on the encrypt flag
        int shift = encrypt ? key : -key;

        // Shift the character and wrap within the ASCII range
        text[i] = (text[i] + shift + 128) % 128; 
    }

    // Output the result
    colored_printf(fgGREEN, bgBLACK, caBOLD, "%s text: %s\n", encrypt ? "Encrypted" : "Decrypted", text);
    printf("\n");
}

int main(int argc, char *argv[]) {
    printf("\e[1;1H\e[2J");

    // Check if the correct number of arguments are passed
    if (argc < 4) {
        colored_printf(fgRED, bgBLACK, caBOLD, "Usage: ./Csar encrypt/decrypt \"text\" key\n");
        printf("\n");

        return 1;
    }

    // Determine mode (encrypt or decrypt) based on the first argument
    int mode = (strcmp(argv[1], "encrypt") == 0) ? 1 : ((strcmp(argv[1], "decrypt") == 0) ? 0 : -1);
    if (mode == -1) {
        colored_printf(fgRED, bgBLACK, caBOLD, "Invalid mode. Use 'encrypt' or 'decrypt'.\n");
        printf("\n");

        return 1;
    }

    // Assign the text and key from command line arguments
    char *text = argv[2];
    int key = atoi(argv[3]); // Convert the key from string to integer

    // Performing the Caesar cipher operation
    caesar_cipher(text, key, mode);
    return 0;
}
