class Solution {
public:
    void reorderList(ListNode* head) {
        // slow fast devide into 2 parts, reverse 2nd part 
        
        //partition
        ListNode *slow=head,*fast=head;
        if(!head || !head->next) return ;
        
        while(fast->next && fast->next->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        
        //reverse
        ListNode *cur=slow->next, *r=NULL,*t;
        slow->next=NULL;
        
        while(cur){
            t=cur->next;
            cur->next=r;
            r=cur;
            cur=t;
        }
        
        //reconstruct
        ListNode *p=head,*q=r;
        while(p && q){
            t=p->next;
            p->next=q;
            q=q->next;
            p=p->next;
            p->next=t;
            p=p->next;
        }
        return ;
    }
};