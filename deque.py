class Deque:
    """
    利用list实现双端队列
    list下标为0的一端代表双端队列的尾端，
    liat下标为-1的一端代表双端队列的首端
    """
    def __init__(self):
        """将双端队列初始化为空列表"""
        self.items = []

    def isEmpty(self):
        return self.items == []

    def appendFront(self, item):
        """从队首添加数据项"""
        self.items.append(item)

    def appendRear(self, item):
        """从队尾添加数据项"""
        self.items.insert(0, item)

    def popFront(self):
        """从队首移除数据项"""
        return self.items.pop()

    def popRear(self):
        """从队尾移除数据项"""
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def testDeque():
    """对双端队列进行测试"""
    deque = Deque()

    print(deque.isEmpty())

    deque.appendRear(123)
    deque.appendRear('abc')
    deque.appendFront(True)
    deque.appendFront(5.2)
    print(deque.size())

    print(deque.popFront())
    print(deque.popRear())

    print(deque.isEmpty())

def palCheck(aString):
    """
    检测回文字串
    :param aString: 待检测的字符串
    :return: True: 是回文字串, False: 不是回文字串
    """
    #如果待检测字符串的长度为1，直接返回True
    if len(aString) == 1: return True
    charDeque = Deque()

    # 将待检测字符串入队
    for char in aString:
        charDeque.appendFront(char)

    while charDeque.size() > 1:
        # 将队首字符和队尾字符出队
        first = charDeque.popFront()
        last = charDeque.popRear()
        if first != last:
            return False

    return True

if __name__ == '__main__':
    testDeque()