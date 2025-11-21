# CC = g++
# CFLAGS = -std=c++11 -Wall
# TARGET = aes_tool
# SRCS = main.cpp AES.cpp FileHandler.cpp Logger.cpp
# OBJS = $(SRCS:.cpp=.o)

# all: $(TARGET)

# $(TARGET): $(OBJS)
# 	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# %.o: %.cpp
# 	$(CC) $(CFLAGS) -c $< -o $@

# clean:
# 	rm -f $(OBJS) $(TARGET) *.log *.enc decrypted_*

# run: $(TARGET)
# 	./$(TARGET)

# test:
# 	@echo "This is a test file for AES encryption" > test.txt
# 	@echo "It contains multiple lines" >> test.txt
# 	@echo "Testing 123!" >> test.txt
# 	@echo "Test file created: test.txt"

# .PHONY: all clean run test

CC = g++
CFLAGS = -std=c++11 -Wall
TARGET = aes_tool.exe
SRCS = main.cpp AES.cpp FileHandler.cpp Logger.cpp
OBJS = $(SRCS:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	del /Q $(OBJS) $(TARGET) *.log *.enc decrypted_*

run: $(TARGET)
	$(TARGET)

test:
	@echo This is a test file for AES encryption > test.txt
	@echo It contains multiple lines >> test.txt
	@echo Testing 123! >> test.txt
	@echo Test file created: test.txt

.PHONY: all clean run test
