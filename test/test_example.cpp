/***********************************************************************
* Copyright 2019, San. All rights reserved.
* Author:  San
* Date:    01/04/2019
***********************************************************************/
#include "gtest/gtest.h"
#include "example.h"

TEST(Example, hello) {
    Example e;

    ASSERT_STREQ(e.hello(), "hello world");
}
