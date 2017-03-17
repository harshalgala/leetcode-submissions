/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pehla = NULL;
        ListNode* badka = head;
        ListNode* temp;
        while(badka!=NULL)
        {
            temp = badka->next;
            badka->next = pehla;
            pehla = badka;
            badka = temp;
        }
        return pehla;
    }
};