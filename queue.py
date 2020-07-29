class Queue:
    """
    利用列表实现队列
    列表首端代表队尾，尾端代表队首
    """
    def __init__(self):
        # 将队列初始化为空列表
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # 将数据item入队
        self.items.insert(0, item)

    def dequeue(self):
        # 将队首元素出队
        return self.items.pop()

    def size(self):
        # 查询队列的长度
        return len(self.items)

    def __str__(self):
        return str(self.items)



def queue_test():
    # 对队列进行测试
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
    模拟传土豆问题
    :param namelist: 参与传土豆的人的名字列表
    :param num: 土豆传递的次数
    :return: 剩余的最后一个人的名字
    """
    trans_queue = Queue()
    for name in namelist:
        trans_queue.enqueue(name)

    while trans_queue.size() > 1:
        # 开始传递
        for _ in range(num):
            trans_queue.enqueue(trans_queue.dequeue())
        # 移除队首
        trans_queue.dequeue()

    return trans_queue.dequeue()

"""模拟打印机问题"""
import random

class Printer:
    """模拟打印机"""
    def __init__(self, ppm):
        """
        初始化打印机，有三个属性，
        pagerate:打印机速度，currentTask:当前打印任务，timeRemaining:当前任务剩余时间
        :param ppm: 打印速度，页数/分钟
        """
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def busy(self):
        # 判断打印机当前是否有打印任务
        return False if self.currentTask == None else True

    def tick(self):
        # 打印机打印一秒
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def startnext(self, newtask):
        # 生成新的打印任务
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task:
    """模拟打印任务"""
    def __init__(self, time):
        """初始化打印任务，有两个属性，timestamp:任务生成时间,pages:打印页数"""
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        # 计算此任务从生成到开始打印的等待时间
        return currentTime - self.timestamp

def newPrinterTask():
    """按照1/180的概率生成打印任务"""
    num = random.randrange(1, 181)
    return True if num == 180 else False

def simualtion(numSeconds, pagesPerMinute):
    """
    打印机运行模拟程序
    :param numSeconds: 总共模拟运行的时间
    :param pagesPerMinute: 打印机的打印速度，即打印模式
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