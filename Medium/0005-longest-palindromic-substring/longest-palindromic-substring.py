class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        maxi = 1
        a = [[0 for x in range(len(s))] for y in range(len(s))]
        
        for i in range(0,l):
            a[i][i] = True
            
        #print a
        begin = 0
        
        for i in range(0,l-1):
            if s[i] == s[i+1]:
                a[i][i+1] = True
                begin = i
                maxi = 2
        #print a
        #print a
        for i in xrange(3,l+1):
            
            for j in xrange(0,l-i+1):
               # print i,j,a
                if s[j] == s[j+i-1] and a[j+1][i+j-2] ==  True:
                    a[j][j+i-1]= True
                    begin = j
                    maxi = i
               
        #print begin,maxi
        return s[begin:begin+maxi]