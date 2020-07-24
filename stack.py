class Stack:
    """���û������ݽṹlistʵ�����ݽṹջ"""
    def __init__(self):
        #��ջ��ʼ��Ϊ���б�
        self.items = []
    
    def isEmpty(self):
        #�ж�ջ�Ƿ�Ϊ��,��ջ�򷵻�True
        return self.items == []
    
    def push(self, item):
        #��itemѹ��ջ��
        self.items.append(item)
    
    def pop(self):
        #��ջ�������Ƴ�
        return self.items.pop()
    
    def peek(self):
        #��ѯ��ǰջ��Ԫ��
        return self.items[-1]
    
    def size(self):
        #��ѯ��ǰջ�ĳ���
        return len(self.items)


def test_stack():
    """��ջ���в���"""
    s = Stack()

    print(s.isEmpty())
    s.push(1)
    s.push("stack")
    print(s.peek())
    print(s.size())
    s.push(True)
    s.push(1.0)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())

#����ƥ��1
def sym_matching(symbol_str):
    """symbol_str:�����������ַ���"""
    #���������ַ����������������ض���ƥ�䣬ֱ�ӷ���false
    if len(symbol_str) % 2 == 1: return False
    #ʹ��Stack֮ǰע���Ƿ���Ҫ����
    s = Stack()
    index = 0
    while index < len(symbol_str):
        if symbol_str[index] in "([{":
            s.push(symbol_str[index])
        else:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not match(top, symbol_str[index]):
                    return False
        index += 1
    return True if s.isEmpty() else False

def match(begin, end):
    begins = "([{"
    ends = ")]}"
    return begins.index(begin) == ends.index(end)

#����ƥ��2
def sym_matching(s):
    if len(s) % 2 == 1: return False
    dict_symbol = {"(":")", "[":"]", "{":"}", "?":"?"}
    stack = Stack()
    stack.push("?")
    for i in s:
        if i in dict_symbol:
            stack.push(i)
        elif dict[stack.pop()] != i:
            return False
    return stack.size() == 1

#����ת��
def base_convert(number, base):
    """
    number����ת����ʮ������
    base����Ҫת���Ľ���
    """
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    
    while number > 0:
        number, rem = divmod(number, base)
        rem_stack.append(rem)
    
    res_string = ""
    while not rem_stack.isEmpty():
        res_string += str(rem_stack.pop())
    
    return res_string