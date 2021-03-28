#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order, and each of their nodes contains a single digit. 
#Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
    #change Linked list to List
    def node2list(self, node1: ListNode) -> List: #linked list -> list
        list1 = []
        while node1 != None :
            list1.append(node1.val)
            node1 = node1.next
        return list1
    
    #change List to Linked List
    def list2node(self, list1: List) -> ListNode:
        result_node = ListNode()
        for i,num in enumerate(list1):
            if i == 0 :
                result_node.val = num
            else :
                node = result_node
                while node.next != None:
                    node = node.next
                node.next = ListNode(num)
        return result_node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.node2list(l1)
        l2 = self.node2list(l2)
        l1 = ''.join(map(str, l1))[::-1]
        l2 = ''.join(map(str, l2))[::-1]
        l3 = list(map(int, list(str(int(l1) + int(l2)))[::-1]))
        
        return self.list2node(l3)
