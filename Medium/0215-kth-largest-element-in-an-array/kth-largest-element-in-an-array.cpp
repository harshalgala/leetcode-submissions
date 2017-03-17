class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        /*for (int i = 0; i < nums.size(); i++)
            cout << nums[i] << " ";*/
        for(int i=0;i<=nums.size();i++)
        {
            if((nums.size()-i)==k)
                return nums[i];
        }
        return nums[0];
    }
    
};