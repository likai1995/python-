class Stack:
    """利用基本数据结构list实现数据结构栈"""
    def __init__(self):
        #将栈初始化为空列表
        self.items = []
    
    def isEmpty(self):
        #判断栈是否为空,空栈则返回True
        return self.items == []
    
    def push(self, item):
        #将item压入栈中
        self.items.append(item)
    
    def pop(self):
        #将栈顶数据移出
        return self.items.pop()
    
    def peek(self):
        #查询当前栈顶元素
        return self.items[-1]
    
    def size(self):
        #查询当前栈的长度
        return len(self.items)


def test_stack():
    """对栈进行测试"""
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

#括号匹配1
def sym_matching(symbol_str):
    """symbol_str:待检测的括号字符串"""
    #如果待检测字符串长度是奇数，必定不匹配，直接返回false
    if len(symbol_str) % 2 == 1: return False
    #使用Stack之前注意是否需要导入
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

#括号匹配2
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

#进制转换
def base_convert(number, base):
    """
    number：待转换的十进制数
    base：将要转换的进制
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