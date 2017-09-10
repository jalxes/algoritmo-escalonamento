#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct process_tag {
        int start;
        char label[2];
        int size;
        int available;
} Process;

Process init_process(int start, char label[2], int size){
        Process self;
        self.start = start;
        strcpy(label, self.label);
        self.size = size;
        self.available = 1;
        return self;
};
Process li[5];
Process exec_li[5];
Process atual;
int volta = 0;
int total_time = 0;
int rr = 3;

void clear(void){
    li[0] = init_process(0, "P1", 8);
    li[1] = init_process(2, "P2", 5);
    li[2] = init_process(4, "P3", 4);
    li[3] = init_process(6, "P4", 2);
    li[4] = init_process(7, "P5", 7);

    atual = NULL;
    exec_li[5] = {0};
    int volta = 0;
    int total_time = len(li);
    int rr = 3;
}


int main(void) {
        clear();
        printf("%d\n", 0);
        return 0;
}
