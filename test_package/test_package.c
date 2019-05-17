#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <libaio.h>

int main() {
    io_context_t ctx;
    memset(&ctx, 0, sizeof(ctx));
    if (io_setup(10, &ctx) != 0) {
        printf("io_setup error\n");
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
