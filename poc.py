list: [
    {
        label: "2",
        size: "2",
    }
    {
    label: "1",
    size: "1",
    }
    {
        label: "3",
        size: "3",
    }
]

def FCFS():
    actualList = list.first
    volta = 0;
    while list:
        volta++
        print "volta " + volta
        self.run(actualList)

def SJNP():
    # TODO: implementar tempo de chegada
    actualList = list.first
    volta = 0;
    while list:
        volta++
        print "volta " + volta
        self.run(actualList)

def SJP():
    actualList = list.first
    volta = 0;
    while list:
        volta++
        print "volta " + volta
        self.run(actualList)

def RR():
    actualList = list.first
    counter = 0;
    input
    while list:
        volta++
        couter++
        if couter >= input:
            actualList = list.next;
        print "volta " + volta
        self.run(actualList)


def run(actualList):
    if actualList.size == 0:
        self.list.remove(actualList);
        actualList = self.list.next()
    actualList.size--
def main():
