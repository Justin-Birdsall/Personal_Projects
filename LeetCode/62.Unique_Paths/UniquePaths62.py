class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
  
    #the first thing that we will have to do is initalize a 2x2 array
    #Since I want to try and use dynamic programing for this initalize the array to m+1 x n+1
    #col before the row - tip from ricky doing something simular in his class 
    #ricky was also explaining to me that for _ in range. you can use the under score a varablie
    #an example would be for a in rage however we don't ever use a again so kind of pointless just do _
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    #now I have an initalized 2d array filled with 0's
        
        #lets also initalize our top left corner to 1 
        dp[1][1] = 1 
#now the goal is to do a tabulation approach (think of fib) you can either do recursive == easier
#or you can memorize the fib sequence in an array and o(1) access it 
        #↓↓↓↓↓ we don't want to underscore in this for loop since we want to use inside itself to access elements
        for i in range(1, m+1):
            for j in range(1, n+1):
                #^^^ this should loop through every index now we just need some checks to properly memorize it

                    #initalize a up and a left variable for comparator
                    #we do this inside the loop since we need to 
                    #reset the check for each itteration/index 
                    up = 0
                    left = 0
                    #we look left and up to see what we should do with the slot we are in 
                    if j-1>=0:
                        left = dp[i][j-1]
                    if i-1>=0:
                        up = dp[i-1][j]
                    #add the summation of up and left to that slot of our table 
                    dp[i][j]=up+left

        return(dp[-1][-1])
