SRC_DIR		= src
OBJ_DIR		= obj
BIN_DIR		= bin
EXE			= $(BIN_DIR)/main
TESTS 		= $(BIN_DIR)/tests
SRC 		= $(wildcard $(SRC_DIR)/*.c)
INCLUDES	= $(wildcard include/*.h)
MAIN_OBJ	= $(OBJ_DIR)/main.o
TEST_OBJ	= $(OBJ_DIR)/euler_test.o
OTHER_OBJ	= $(OBJ_DIR)/euler.o
CC 			= gcc
CFLAGS		= -Wall -Wextra -Werror -g -std=c11 -pedantic
CPPFLAGS	= -Iinclude -MMD -MP
LDFLAGS 	= -Llib
LDLIBS		= -lm

ifeq ($(OS),Windows_NT)
	RM = erase /q /s
else
	RM = rm -f -rv
endif

all: $(EXE) $(TESTS)

.PHONY: all clean

$(EXE): $(MAIN_OBJ) $(OTHER_OBJ) | $(BIN_DIR)
	$(CC) -o $@ $(LDFLAGS) $^ $(LDLIBS)

$(TESTS): $(TEST_OBJ) $(OTHER_OBJ) | $(BIN_DIR)
	$(CC) -o $@ $(LDFLAGS) $^ $(LDLIBS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

$(OBJ_DIR):
	mkdir $@

$(BIN_DIR):
	mkdir $@

clean:
	@$(RM) $(OBJ_DIR) $(BIN_DIR)

-include $(OBJ:.o=.d)
