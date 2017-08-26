class Process:
    def __init__(self, start, label, size):
        self.start = start
        self.label = label
        self.size = size
        self.available = True
li = [Process(num,num,num*2) for num in range(3)]
execLi = []
volta = 0;
execLi.append(li[0])
atual = execLi[0]
totalTime = len(li)
while True:
    if totalTime <= 0:
        break
    for value in li:
        if value.start == volta & value.available:
            execLi.append(value)
            value.available = False
    if len(execLi):
        atual.size -= 1
        if atual.size <= 0:
            totalTime -= 1
            execLi.remove(atual)
            atual = execLi[0]
    # print("totalTime ", totalTime)
    # print("volta ", volta)
    # print("atual ", atual.label)
    # print("size ", atual.size)
    # print("------")
    volta += 1
    for value in execLi:
        print(value.label)
