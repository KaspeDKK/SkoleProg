# Compiler and flags
CC=gcc
CFLAGS=-Wall -g

# Your program's final executable name
TARGET=csar

# All source files
SRCS=Csar.c colors.c
OBJS=$(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Rule to create executable from object files
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Rule to create object files from C source files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up
clean:
	rm -f $(TARGET) $(OBJS)
