class Node(object):
    """
    定义节点类
    data: 节点存储的数据
    pnext: 保存下一节点对象
    """
    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        """
        重构输出方法，对比__str__方法
        将self.data按照字符串输出
        """
        return str(self.data)

class ChainTable(object):
    """
    定义链表类
    """
    def __init__(self):
        """初始化空链表，头结点的指向为None，链表长度为0"""
        self.head = None
        self.length = 0

    def isEmpty(self):
        """
        判断链表是否为空链表
        :return: True：空链表
        """
        return self.length == 0

    def append(self, dataOrNode):
        """
        链表末端添加节点
        :param dataOrNode: 待添加的节点或数据
        :return:
        """
        #判断参数是不是节点类，不是节点的话要以参数为数据变量建立节点
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        #链表是空链表，直接将新节点作为第一个结点
        if not self.head:
            self.head = item
            self.length += 1
        #链表不为空，遍历到链表末尾添加
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    def delete(self, index):
        """
        按索引删除节点
        :param index: 待删除节点的索引号
        :return:
        """
        #判断可能的异常情况
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        #如果删除的是头结点，直接将头结点指向头结点的下一项
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        #否则，遍历链表至删除的位置，将删除节点的前一项指向删除节点的下一项
        j = 0
        node = self.head
        pnext = self.head
        while node.next and j < index:
            pnext = node
            node = node.next
            j += 1
        if j == index:
            pnext.next = node.next
            self.length -= 1

    def insert(self, index, dataOrNode):
        """
        在链表的index位置插入节点
        :param index: 新节点的插入位置
        :param dataOrNode: 插入的节点或数据
        :return:
        """
        #判断可能的异常情况
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        #判断dataOrNode的类型
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        #如果插入位置是头结点，新节点指向原来的头结点，更新头结点为新节点，链表长度+1
        if index == 0:
            item.next = self.head
            self.head = item
            self.length += 1
            return

        #否则，遍历链表至新节点要添加的位置，老节点与前节点的连接，插入新节点，前节点指向新节点，新节点指向旧节点
        j = 0
        node = self.head
        pnext = self.head
        while node.next and j < index:
            pnext = node
            node = node.next
            j += 1
        if j == index:
            item.next = node
            pnext.next = item
            self.length += 1

    def update(self, data, index):
        """
        更新指定位置的节点值
        :param data: 新的节点数据
        :param index: 待更新节点的索引
        :return:
        """
        #判断异常情况
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        #遍历链表至更新位置，更改节点值
        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1
        if j == index:
            node.data = data

    def getItem(self, index):
        """
        根据索引查找节点数据
        :param index: 查找节点的索引
        :return: 节点存储的数据
        """
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1

        return node.data

    def getIndex(self, data):
        """
        根据数据查找节点索引
        :param data: 节点数据
        :return: 节点索引
        """
        if self.isEmpty():
            print("thie chain table is empty")
            return

        j = 0
        node = self.head
        while node:
            if node.data == data:
                return j
            else:
                node = node.next
                j += 1

        if j == self.length:
            print("%s not found" % str(data))
            return

    def clear(self):
        """清空链表"""
        self.head = None
        self.length = 0


    def __repr__(self):
        """
        重构输出方法
        :return: 按数据+空格方式输出
        """
        if self.isEmpty():
            return "empty chain table"
        j = 0
        node = self.head
        nlist = ' '
        while node and j < self.length+5:
            nlist += str(node.data) + ' '
            node = node.next
            j += 1
        return nlist

    def __getitem__(self, index):
        """
        重构get方法
        :param item: 节点索引
        :return: 节点数据
        """
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        return self.getItem(index)

    def __setItem__(self, data, index):
        """
        重构新增节点方法
        :param data: 新增节点数据
        :param index: 新增节点索引
        :return:
        """
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return
        self.update(data, index)

    def __len__(self):
        """
        重构链表长度方法
        :return: 链表长度
        """
        return self.length



def test_chaintable():
    """测试链表类"""
    chaintable = ChainTable()

    print(chaintable.isEmpty())

    for i in range(10):
        chaintable.append(i)

    print(chaintable)
    print(len(chaintable))

    chaintable.update(10, 1)
    print(chaintable)

    chaintable.delete(3)
    print(chaintable)

    chaintable.insert(3, 30)
    print(chaintable)

    print(chaintable.getItem(3))
    print(chaintable[3])

    chaintable.insert(0, 100)
    print(chaintable)

    print(chaintable.head)

if __name__ == '__main__':
    test_chaintable()