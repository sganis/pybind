#include "gtest/gtest.h"
#include "example.h"


TEST(Example, hello)
{
    Example e;
    ASSERT_STREQ(e.hello(), "hello world");
}
