class Process:
    def __init__(self, start, label, size):
        self.start = start
        self.label = label
        self.size = size
        self.available = True


def load(i):
    if len(li) <= i:
        return
    for value in li:
        if value.start == i & value.available:
            execLi.append(li[i])
            li[i].available = False


li = [Process(num, num, num + 1 * 2) for num in range(3)]
execLi = []
volta = 0
totalTime = len(li)
print(len(li))

while True:
    if totalTime <= 0:
        break
    load(volta)
    if not 'atual' in vars():
        atual = execLi[volta]
    print("volta ", volta, ", li ", atual.label, atual.size)
    if atual:
        atual.size -= 1
        if atual.size <= 0:
            print("cut the shit out , li ", atual.label, atual.size)
            totalTime -= 1
            execLi.remove(atual)
            if len(execLi):
                atual = execLi[0]
    # print("totalTime ", totalTime)
    # print("volta ", volta)
    # print("atual ", atual.label)
    # print("size ", atual.size)
    # print("------")
    volta += 1
