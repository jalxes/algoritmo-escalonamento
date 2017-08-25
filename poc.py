class Process:
    def __init__(self, start, label, size):
        self.start = start
        self.label = label
        self.size = size


li = [Process(num,num,num) for num in range(3)]
execList = []
currentLi = []

def FCFS():
    currentLi = first(li)
    volta = 0;
    while True:
        load(volta)
        if not len(exec):
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
#
# def first(li):
#     return x1
# def next(li):
#     return x1
#
# def load(i):
#     if li[i]:
#         execLi.append(li[i])
#
# def run(item):
#     if not item.size == 0:
#         li.remove(item);
#         item = next(li)
#     item.size-=1
#
def main():
    FCFS()
    # SJNP()
    # SJP()
    # RR()
main()
