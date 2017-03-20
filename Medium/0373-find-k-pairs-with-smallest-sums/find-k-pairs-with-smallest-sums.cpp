class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
         vector<pair<int,int>> res;
        vector<int> pos(nums1.size());
        int sz1 = nums1.size(), sz2 = nums2.size();
        int cnt  = 0;
        if(sz1 == 0 || sz2== 0)
            return res;
        
        
        while(cnt < k){
            int minSum = INT_MAX;
            int nxt = -1;
            for(int j = 0; j < sz1; j++){
                if(pos[j] < sz2 && nums1[j]+ nums2[pos[j]] < minSum){
                    nxt = j;
                    minSum =nums1[j]+ nums2[pos[j]]; 
                }
            }
            if(nxt == -1){
                break;
            }
            res.push_back(make_pair(nums1[nxt], nums2[pos[nxt]]));
            pos[nxt]++;
            cnt++;
        }
        
        return res;
    }
};