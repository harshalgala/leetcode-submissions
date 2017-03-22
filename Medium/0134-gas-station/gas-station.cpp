class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int leftover = 0;
        int total = 0;
        int begin = 0;
        
        for(int i=0;i<gas.size();i++)
        {
            int remain = gas[i] - cost[i];
            
            if(leftover>=0)
                leftover +=remain;
            else
            {
                leftover = remain;
                begin = i;
            }
            total += remain;
        }
        if(total>=0)
        {
            return begin;
        }
        else
        {
            return -1;
        }
    }
};