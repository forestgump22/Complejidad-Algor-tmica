
def fibonnaci(i):
    #base cases;
    memo={};
    memo[0]=1;
    memo[1]=1;
    def dp(i):  
        if i not in memo:
            memo[i]=dp(i-1)+dp(i-2);
        return memo[i];
    return dp(i);
#easy
def practiceFibonaci():
    print(fibonnaci(98));

def contingstairs(i):
    #base cases;
    memo={};
    memo[1]=1;
    memo[2]=2;
    memo[3]=3;
    def dp(i):
        if i not in memo:
            memo[i]=dp(i-1)+dp(i-2);
        return memo[i];
    return dp(i);
def houserob(houses):
    #bases;
    memo={};
    memo[0]=houses[0];
    memo[1]=max(houses[0],houses[1]);
    def dp(i):
        if i not in memo:
            memo[i]= max(houses[i]+dp(i-2),dp(i-1));
        return memo[i];
    return dp(len(houses)-1);
def deleteAndEarn(arr):
    dp=[0]*max(arr);
    for num in arr:
        dp[num]=+num;
    return houserob(dp);
def matchingpatterns(s,p):
    memo={()};
    def decisiontree(i,j):
        if (i,j) in memo:
            return memo[(i,j)];
        if i>=len(s) and j>=len(p):
            return True;
        if j>=len(p):
            return False;
        match= ((i<len(s) and (s[i]==p[j] or p[j]==".")));
        if (j+1<len(p) and p[j+1]=="*"):
            memo[(i,j)]=decisiontree(i,j+2) or \
                        (match and decisiontree(i+1,j));
            return memo[(i,j)];
        if match:
            memo[(i,j)]= decisiontree(i+1,j+1);
            return memo[(i,j)];
        memo[(i,j)]=False;
        return memo[(i,j)];
    return decisiontree(0,0);
if __name__=="__main__":
    practiceFibonaci();