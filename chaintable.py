class Node(object):
    """
    ����ڵ���
    data: �ڵ�洢������
    pnext: ������һ�ڵ����
    """
    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        """
        �ع�����������Ա�__str__����
        ��self.data�����ַ������
        """
        return str(self.data)

class ChainTable(object):
    """
    ����������
    """
    def __init__(self):
        """��ʼ��������ͷ����ָ��ΪNone��������Ϊ0"""
        self.head = None
        self.length = 0

    def isEmpty(self):
        """
        �ж������Ƿ�Ϊ������
        :return: True��������
        """
        return self.length == 0

    def append(self, dataOrNode):
        """
        ����ĩ����ӽڵ�
        :param dataOrNode: ����ӵĽڵ������
        :return:
        """
        #�жϲ����ǲ��ǽڵ��࣬���ǽڵ�Ļ�Ҫ�Բ���Ϊ���ݱ��������ڵ�
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        #�����ǿ�����ֱ�ӽ��½ڵ���Ϊ��һ�����
        if not self.head:
            self.head = item
            self.length += 1
        #����Ϊ�գ�����������ĩβ���
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    def delete(self, index):
        """
        ������ɾ���ڵ�
        :param index: ��ɾ���ڵ��������
        :return:
        """
        #�жϿ��ܵ��쳣���
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        #���ɾ������ͷ��㣬ֱ�ӽ�ͷ���ָ��ͷ������һ��
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        #���򣬱���������ɾ����λ�ã���ɾ���ڵ��ǰһ��ָ��ɾ���ڵ����һ��
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
        �������indexλ�ò���ڵ�
        :param index: �½ڵ�Ĳ���λ��
        :param dataOrNode: ����Ľڵ������
        :return:
        """
        #�жϿ��ܵ��쳣���
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        #�ж�dataOrNode������
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        #�������λ����ͷ��㣬�½ڵ�ָ��ԭ����ͷ��㣬����ͷ���Ϊ�½ڵ㣬������+1
        if index == 0:
            item.next = self.head
            self.head = item
            self.length += 1
            return

        #���򣬱����������½ڵ�Ҫ��ӵ�λ�ã��Ͻڵ���ǰ�ڵ�����ӣ������½ڵ㣬ǰ�ڵ�ָ���½ڵ㣬�½ڵ�ָ��ɽڵ�
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
        ����ָ��λ�õĽڵ�ֵ
        :param data: �µĽڵ�����
        :param index: �����½ڵ������
        :return:
        """
        #�ж��쳣���
        if self.isEmpty():
            print("thie chain table is empty")
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return

        #��������������λ�ã����Ľڵ�ֵ
        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1
        if j == index:
            node.data = data

    def getItem(self, index):
        """
        �����������ҽڵ�����
        :param index: ���ҽڵ������
        :return: �ڵ�洢������
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
        �������ݲ��ҽڵ�����
        :param data: �ڵ�����
        :return: �ڵ�����
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
        """�������"""
        self.head = None
        self.length = 0


    def __repr__(self):
        """
        �ع��������
        :return: ������+�ո�ʽ���
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
        �ع�get����
        :param item: �ڵ�����
        :return: �ڵ�����
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
        �ع������ڵ㷽��
        :param data: �����ڵ�����
        :param index: �����ڵ�����
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
        �ع������ȷ���
        :return: ������
        """
        return self.length



def test_chaintable():
    """����������"""
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