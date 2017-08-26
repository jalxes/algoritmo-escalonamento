class Process:
    def __init__(self, start, label, size):
        self.start = start
        self.label = label
        self.size = size
currentLi = Process()

def fixture():
    li = [Process(num,num,num) for num in range(3)]
    execLi = []
    currentLi = Process()

def FCFS():
    volta = 0;
    while True:
        load(volta)
        if not len(execLi):
            break
        volta += 1
        print("volta ", volta)
        run(currentLi)
#
# def SJNP():
#     # TODO: implementar tempo de chegada
#     currentLi = first(li)
#     volta = 0;
#     while li:
#         volta += 1
#         print("volta ", volta)
#         run(currentLi)
#
# def SJP():
#     currentLi = first(li)
#     volta = 0;
#     while li:
#         volta += 1
#         print("volta ", volta)
#         run(currentLi)
#
# def RR():
#     currentLi = first(li)
#     counter = 0;
#     input
#     while li:
#         volta += 1
#         couter += 1
#         if couter >= input:
#             currentLi = next(li)
#             couter = 0
#         print("volta ", volta)
#         run(currentLi)

def first():
    back = li[0]
    return back

def load(i):
    if li[i]:
        execLi.append(li[i])

def run(item):
    if item.size == 0:
        execLi.remove(item);
        item = next(execLi)
    item.size-=1

def main():
    fixture()
    volta = 0;
    while True:
        load(volta)
        if not len(execLi):
            break
        volta += 1
        print("volta ", volta)
        runFCFS(currentLi)

    # SJNP()
    # SJP()
    # RR()
main()
