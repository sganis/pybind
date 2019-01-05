/***********************************************************************
* Copyright 2019, San. All rights reserved.
* Author:  San
* Date:    01/04/2019
***********************************************************************/
#include <iostream>
#include <string.h>
#include <example.h>
#include "version.h"

int main(int argc, char** argv) {
    if ((argc > 1) && (strcmp(argv[1], "--version") == 0)) {
        printf("%s Version %s\n", argv[0], VERSION);
        return 1;
    }
    Example e;
    printf("Example: %s\n", e.hello());
    return 0;
}
