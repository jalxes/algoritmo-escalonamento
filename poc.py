class Process:
    def __init__(self, start, label, size):
        self.start = start
        self.label = label
        self.size = size

if __name__ == "__main__":
    x1 = Process(1,1,1)
    x2 = Process(2,2,2)
    x3 = Process(3,3,3)

li = [x1, x2, x3]
execList = []
currentLi = [x1, x2, x3]
def FCFS():
    currentLi = first(li)
    volta = 0;
    while True:
        if not len(li):
            break
        volta += 1
        print("volta ", volta)
        run(currentLi)

def SJNP():
    # TODO: implementar tempo de chegada
    currentLi = first(li)
    volta = 0;
    while li:
        volta += 1
        print("volta ", volta)
        run(currentLi)

def SJP():
    currentLi = first(li)
    volta = 0;
    while li:
        volta += 1
        print("volta ", volta)
        run(currentLi)

def RR():
    currentLi = first(li)
    counter = 0;
    input
    while li:
        volta += 1
        couter += 1
        if couter >= input:
            currentLi = next(li)
            couter = 0
        print("volta ", volta)
        run(currentLi)

def first(li):
    return x1
def next(li):
    return x1

def run(item):
    if not item.size == 0:
        li.remove(item);
        item = next(li)
    item.size-=1

def main():
    FCFS()
    SJNP()
    SJP()
    RR()
main()
