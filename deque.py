class Deque:
    """
    ����listʵ��˫�˶���
    list�±�Ϊ0��һ�˴���˫�˶��е�β�ˣ�
    liat�±�Ϊ-1��һ�˴���˫�˶��е��׶�
    """
    def __init__(self):
        """��˫�˶��г�ʼ��Ϊ���б�"""
        self.items = []

    def isEmpty(self):
        return self.items == []

    def appendFront(self, item):
        """�Ӷ������������"""
        self.items.append(item)

    def appendRear(self, item):
        """�Ӷ�β���������"""
        self.items.insert(0, item)

    def popFront(self):
        """�Ӷ����Ƴ�������"""
        return self.items.pop()

    def popRear(self):
        """�Ӷ�β�Ƴ�������"""
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def testDeque():
    """��˫�˶��н��в���"""
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
    �������ִ�
    :param aString: �������ַ���
    :return: True: �ǻ����ִ�, False: ���ǻ����ִ�
    """
    #���������ַ����ĳ���Ϊ1��ֱ�ӷ���True
    if len(aString) == 1: return True
    charDeque = Deque()

    # ��������ַ������
    for char in aString:
        charDeque.appendFront(char)

    while charDeque.size() > 1:
        # �������ַ��Ͷ�β�ַ�����
        first = charDeque.popFront()
        last = charDeque.popRear()
        if first != last:
            return False

    return True

if __name__ == '__main__':
    testDeque()