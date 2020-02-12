#链表的定义
class ListNode():
    def __init__(self, val):
        if isinstance(val,int):
            self.val = val
            self.next = None
            
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            cur = self  #引入cur，方便做self(实例)的next.next。。。处理
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
    
    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
            return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"


#Note:我们不断的遍历两个链表，每次遍历都将链表a和链表b的值相加，再赋给链表a。如果有进位我们还需要记录一个进位标志。
#循环的条件是链表a不为空或者链表b不为空，这样当整个循环结束时，链表就被串起来了。
#当循环结束时，如果进位标志>0还需要处理下边界条件。
#我们不用生成一个新的节点，直接将两个节点相加的值赋给节点a就可以了，这样只用改变节点的内容，速度会更快一些。
#i.e.还有准确来说使用节点时候，默认是使用a节点的，如果a节点为空了，就用b节点。相当于是用l1,l2链表的原内存空间构成目标内内存，优先使用l1链表的空间。

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #不过就算我们定义了这个类，在本地调试的过程中，我们传参的形式还是list。但是在leetcode提交代码并不是，而是应该官方通过接口将我们传入的[1,2,3]list形式参数转化成了ListNode了。
        if isinstance(l1,list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)


        a,b,p,carry = l1, l2, None, 0
        while a or b:
            # a和b节点的值相加，如果有进位还要加上进位的值
            val = (a.val if a else 0) + (b.val if b else 0) + carry
            # 根据val判断是否有进位,不管有没有进位，val都应该小于10
            carry, val = int(val/10) if val >= 10 else 0, val%10
            p,p.val = a if a else b, val
            # a 和 b指针都进一位
            a,b = a.next if a else None, b.next if b else None
            #根据a和b是否为空，p指针也前进一位
            p.next = a if a else b
        # 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件
        if carry:
            p.next = ListNode(carry)
        return l1
    
    
    #我们来看看vscode调试打印的效果
    """if __name__ == "__main__":
        test = Solution()
        print('我们来看看vscode调试打印的效果:',test.addTwoNumbers([1,3],[2,1,3]))"""

    






print(Solution.addTwoNumbers(ListNode([1,2,3,4,5]),ListNode([2,3,4,5,6]),ListNode([2,3,4,5,6])))


 