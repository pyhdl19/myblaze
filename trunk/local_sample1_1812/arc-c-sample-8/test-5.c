/*
 * test.c
 */

volatile unsigned int * sigptr = (unsigned int *)0xffffffc0;
volatile unsigned int i = 1;
volatile unsigned int j = 2;
volatile int cumuloops = 3;

int main() {
    register int a = 0;
    for (i=0; i<10; i++) {
        for (j=0; j<4; j++) {
            a ++;
        }
        *sigptr = i;
        cumuloops ++;
    }
    return cumuloops + a;
}


