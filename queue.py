class Queue:
    """
    �����б�ʵ�ֶ���
    �б��׶˴����β��β�˴������
    """
    def __init__(self):
        # �����г�ʼ��Ϊ���б�
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # ������item���
        self.items.insert(0, item)

    def dequeue(self):
        # ������Ԫ�س���
        return self.items.pop()

    def size(self):
        # ��ѯ���еĳ���
        return len(self.items)

    def __str__(self):
        return str(self.items)



def queue_test():
    # �Զ��н��в���
    q = Queue()

    print(q.isEmpty())
    q.enqueue(123)
    q.enqueue('abc')
    q.enqueue(True)
    print(q)
    print(q.size())
    q.dequeue()
    q.dequeue()
    print(q.isEmpty())
    print(q)

def hot_potato(namelist, num):
    """
    ģ�⴫��������
    :param namelist: ���봫�������˵������б�
    :param num: �������ݵĴ���
    :return: ʣ������һ���˵�����
    """
    trans_queue = Queue()
    for name in namelist:
        trans_queue.enqueue(name)

    while trans_queue.size() > 1:
        # ��ʼ����
        for _ in range(num):
            trans_queue.enqueue(trans_queue.dequeue())
        # �Ƴ�����
        trans_queue.dequeue()

    return trans_queue.dequeue()

"""ģ���ӡ������"""
import random

class Printer:
    """ģ���ӡ��"""
    def __init__(self, ppm):
        """
        ��ʼ����ӡ�������������ԣ�
        pagerate:��ӡ���ٶȣ�currentTask:��ǰ��ӡ����timeRemaining:��ǰ����ʣ��ʱ��
        :param ppm: ��ӡ�ٶȣ�ҳ��/����
        """
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def busy(self):
        # �жϴ�ӡ����ǰ�Ƿ��д�ӡ����
        return False if self.currentTask == None else True

    def tick(self):
        # ��ӡ����ӡһ��
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def startnext(self, newtask):
        # �����µĴ�ӡ����
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task:
    """ģ���ӡ����"""
    def __init__(self, time):
        """��ʼ����ӡ�������������ԣ�timestamp:��������ʱ��,pages:��ӡҳ��"""
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        # �������������ɵ���ʼ��ӡ�ĵȴ�ʱ��
        return currentTime - self.timestamp

def newPrinterTask():
    """����1/180�ĸ������ɴ�ӡ����"""
    num = random.randrange(1, 181)
    return True if num == 180 else False

def simualtion(numSeconds, pagesPerMinute):
    """
    ��ӡ������ģ�����
    :param numSeconds: �ܹ�ģ�����е�ʱ��
    :param pagesPerMinute: ��ӡ���Ĵ�ӡ�ٶȣ�����ӡģʽ
    :return:
    """
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrinterTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if not labprinter.busy() and not printQueue.isEmpty():
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startnext(nexttask)

        labprinter.tick()

    averageWaitTime = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." \
          % (averageWaitTime, printQueue.size()))