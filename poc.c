#include <stdio.h>


typedef struct process_tag {
    int start;
    int label;
    int size;
    int available;
} Process;

Process init_process(int start, int label, int size){
    Process self;
    self->start = start;
    self->label = label;
    self->size = size;
    self->available = True;
    return self;
};
li = []
exec_li = []
int volta = 0
int total_time = 0
int rr = 3

void clear():

    li = [
        init_process(0, "P1", 8),
        init_process(2, "P2", 5),
        init_process(4, "P3", 4),
        init_process(6, "P4", 2),
        init_process(7, "P5", 7)
    ]

    atual = None
    exec_li = []
    volta = 0
    total_time = len(li)
    rr = 3


int main(void) {
    printf("%d\n", 0);
    return 0;
}
