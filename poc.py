from random import randint


class Process:
    def __init__(self, start, label, size):
        self.start = start
        self.label = label
        self.size = size
        self.available = True


li = []
exec_li = []
volta = 0
total_time = 0
rr = 3

def clear():

    global li
    global exec_li
    global volta
    global total_time
    global atual
    global rr
    li = [
        Process(0, 0, 3),
        Process(1, 1, 9),
        Process(2, 2, 1),
        Process(3, 3, 5)
    ]

    atual = None
    exec_li = []
    volta = 0
    total_time = len(li)
    rr = 3

def load(i):
    if len(li) <= i:
        return
    for value in li:
        if value.start == i & value.available:
            exec_li.append(li[i])
            li[i].available = False


def defAtual(modo):
    global rr
    if not 'atual' in globals():
        global atual
    if not atual in exec_li:
        if len(exec_li):
            atual = exec_li[0]
            rr = 3
    if (modo == 'FCFS'):
        return
    if (modo == 'SJNP'):
        if atual.available:
            atual.available = False
            minor = atual
            for value in exec_li:
                if minor.size > value.size:
                    minor = value
            atual = minor
    if (modo == 'SJP'):
        minor = atual
        for value in exec_li:
            if minor.size > value.size:
                minor = value
        atual = minor
    if(modo == "RR"):
        rr -= 1
        if rr <= 0:
            rr = 3
            if len(exec_li) > 1:
                index = exec_li.index(atual)
                print(index)
                print(len(exec_li))
                if index >= len(exec_li)-1:
                    index = -1
                atual = exec_li[index + 1]
# def FCFS():
# def SJNP():
# def SJP():
# def RR():


def main(modo):
    global i
    global exec_li
    global volta
    global total_time
    global atual
    clear()

    print('modo: ', modo)
    while True:
        if volta > 100:
            break
        if total_time <= 0:
            break
        # print("volta ", volta)
        load(volta)
        defAtual(modo)
        if atual:
            print("li ", atual.label, atual.size)
            atual.size -= 1
            if atual.size < 0:
                total_time -= 1
                exec_li.remove(atual)
                if len(exec_li):
                    atual = exec_li[0]
                    atual.available = True
        # print("total_time ", total_time)
        # print("volta ", volta)
        # print("atual ", atual.label)
        # print("size ", atual.size)
        # print("------")
        volta += 1


main('FCFS')
main('SJNP')
main('SJP')
main('RR')
