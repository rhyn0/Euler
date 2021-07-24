SRC_DIR		= src
OBJ_DIR		= obj
BIN_DIR		= ..
EXE			= $(BIN_DIR)\\main
TESTS 		= $(BIN_DIR)\\tests
SRC 		= $(wildcard $(SRC_DIR)/*.c)
INCLUDES	= $(wildcard include/*.h)
CC 			= gcc
CFLAGS		= -pedantic -Wall -Wextra -Werror -g -std=c17
CPPFLAGS	= -Iinclude -MMD -MP
LDFLAGS 	= -Llib
LDLIBS		= -lm

all: $(EXE) $(TESTS)

.PHONY: all

$(EXE): obj/euler.o obj/main.o
	$(CC) -o $@ $(LDFLAGS) $^ $(LDLIBS)

$(TESTS): obj/euler_test.o obj/euler.o
	$(CC) -o $@ $(LDFLAGS) $^ $(LDLIBS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

$(OBJ_DIR):
	mkdir -p $@

clean:
	@$(RM) -rv $(OBJ_DIR)

-include $(OBJ:.o=.d)