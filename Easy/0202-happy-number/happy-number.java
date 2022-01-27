class Solution {
    public boolean isHappy(int n) {
        Set<Integer> look = new HashSet<>();
        while (n!=1 && !look.contains(n))
        {
            look.add(n);
            n = getSumSquares(n);
        }
        return n == 1;
    }
    public int getSumSquares(int n)
    {
        int totalNum=0;
        while (n>0) {
            int lastDigit = n%10;
            totalNum += lastDigit*lastDigit;
            n=n/10;
        }
        return totalNum;
    }
    
}