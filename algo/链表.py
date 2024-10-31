
class ListNode:
    """链表节点类"""
    def __init__(self, val):
        self.val = val               # 节点值
        self.next = None # 指向下一节点的引用
    
# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
# 初始化各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    
    P.next = n1
    n0.next = P
p=ListNode(10)
insert(n1,p)
def access(head: ListNode, index: int) :#访问节点需要从头节点出发
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head.val
print(access(n0,2))