
def mergeLists(head1, head2):
    
    # if list1 is empty, return list2
    # if list2 is empty, return list1
    if not head1:
        return head2
    elif not head2:
        return head1
        
    while head1 and head2:
        if head1.data < head2.data:
           head1.next = mergeLists(head1.next, head2)
           return head1
        # if head1.data > head2.data
        else:
            head2.next = mergeLists(head2.next, head1)
            return head2
