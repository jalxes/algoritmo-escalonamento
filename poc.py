class Process:
    def __init__(self, start, label, size):
        self.start = start
        self.label = label
        self.size = size

list: [
    {
        "startAt": "2",
        "label": "2",
        "size": "2",
    },
    {
        "startAt": "1",
        "label": "1",
        "size": "1",
    },
    {
        "startAt": "3",
        "label": "3",
        "size": "3",
    }
    def list():
        pass
]
execList: []

def FCFS():
    actualList = self.first(list)
    volta = 0;
    while list:
        volta += 1
        print ("volta " + volta)
        self.run(actualList)

def SJNP():
    # TODO: implementar tempo de chegada
    actualList = self.first(list)
    volta = 0;
    while list:
        volta += 1
        print( "volta " + volta)
        self.run(actualList)

def SJP():
    actualList = self.first(list)
    volta = 0;
    while list:
        volta += 1
        print( "volta " + volta)
        self.run(actualList)

def RR():
    actualList = self.first(list)
    counter = 0;
    input
    while list:
        volta += 1
        couter += 1
        if couter >= input:
            actualList = list.next
            couter = 0
        print( "volta " + volta)
        self.run(actualList)
def first(list):
    pass
def run(actualList):
    if actualList.size == 0:
        self.list.remove(actualList);
        actualList = self.next(list)
    actualList.size-=1
def main():
    FCFS()
    SJNP()
    SJP()
    RR()
main()
