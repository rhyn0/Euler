#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "euler.h"
#include "acutest.h"

void test_euler1(void)
{
    TEST_CHECK_(euler1(-1) == 233168, "euler1(%d)==%d", -1, 233168);
}

TEST_LIST = {
    {"int euler1(int);", test_euler1},
    {0} // according to acutest, must do this
};
