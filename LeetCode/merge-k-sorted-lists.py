# https://leetcode.com/problems/merge-k-sorted-lists/

# 1. use heapq

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list['ListNode']) -> 'ListNode':
        min_heap = []
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next


----------------------------------------------------------------------------

# 2. stupid way

class Solution:
    def mergeKLists(self, lists: list['ListNode']) -> 'ListNode':
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        
        values.sort()
        
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
