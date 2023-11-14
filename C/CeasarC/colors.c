/**
 * File: colors.c
 * Author: KaspeDKK - <https://github.com/kaspedkk>
 * 
 * Description: TBD
 */

#include <stdio.h>
#include <stdarg.h>

void setcolors(int foreground, int background, int attribute)
{
  	printf("\033[%i;%i;%im", attribute, foreground, background);  
}

void resetcolors(void)
{
  	printf("\033[0m");  
}

void moveUp(int positions) {
    printf("\x1b[%dA", positions);
}
 
void moveDown(int positions) {
	printf("\x1b[%dB", positions);
}
 
void moveRight(int positions) {
 	printf("\x1b[%dC", positions);
}
 
void moveLeft(int positions) {
 	printf("\x1b[%dD", positions);
}
 
void moveTo(int row, int col) {
 	printf("\x1b[%d;%df", row, col);
}

void colored_printf(int foreground, int background, int attribute, const char *format, ...) {
    va_list args;
    va_start(args, format);

    setcolors(foreground, background, attribute);
    vprintf(format, args);
    resetcolors();

    va_end(args);
}