# https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  sum_list = ListNode.new()
  h = sum_list
  carry = false
  while l1 != nil || l2 != nil || carry
    sum = 0
    if l1 != nil
      sum += l1.val
      l1 = l1.next
    end
    if l2 != nil
      sum += l2.val
      l2 = l2.next
    end
    if carry
      sum += 1
    end
    h.next = ListNode.new(sum%10)
    h = h.next
    carry = sum>=10 ? true : false
  end
  return sum_list.next
end