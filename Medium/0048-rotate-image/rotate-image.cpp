class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int size = matrix[0].size();
        //for(int k=0;k<size/2;k++){
        for(int i=0;i<size/2;i++){
            for(int j=i;j<size-i-1;j++){
                int temp = matrix[i][j];
                matrix[i][j]=matrix[abs(size-1-j)][i];
                matrix[abs(size-1-j)][i] = matrix[abs(size-1-i)][abs(size-1-j)];
                matrix[abs(size-1-i)][abs(size-1-j)] = matrix[j][abs(size-1-i)];
                matrix[j][abs(size-1-i)]= temp;
            }
        }
    //}
        
    }
};