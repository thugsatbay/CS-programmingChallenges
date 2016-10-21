'''

A word from the English dictionary is taken and arranged as a matrix. e.g. "MATHEMATICS"

MATHE  
ATHEM  
THEMA  
HEMAT  
EMATI  
MATIC  
ATICS  
There are many ways to trace this matrix in a way that helps you construct this word. You start tracing the matrix from the top-left position and at each iteration, you either move RIGHT or DOWN, and ultimately reach the bottom-right of the matrix. It is assured that any such tracing generates the same word. How many such tracings can be possible for a given word of length m+n-1 written as a matrix of size m * n?

Input Format 
The first line of input contains an integer T. T test cases follow. 
Each test case contains 2 space separated integers m & n (in a new line) indicating that the matrix has m rows and each row has n characters.

Constraints 
1 <= T <= 103 
1 ≤ m,n ≤ 106

Output Format 
Print the number of ways (S) the word can be traced as explained in the problem statement. If the number is larger than 109+7, 
print S mod (10^9 + 7) for each testcase (in a new line).

Sample Input

1
2 3
Sample Output

3

'''






import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
def findTrac(posOff,m,n):
    state=[posOff]
    sol=0
    while (len(state)>0):
        push=state[0]
        state=state[1:]
        if push[0]==m-1 or push[1]==n-1:
            sol+=1
        else:
            state.append([push[0]+1,push[1]])
            state.append([push[0],push[1]+1])
    return sol
    #if posOff[0]==m-1 or posOff[1]==n-1:
        #return 1
    #return findTrac([posOff[0]+1,posOff[1]],m,n) + findTrac([posOff[0],posOff[1]+1],m,n)

#(N-1+M-1)!/((N-1)!(M-1)!)
def factTrac(m,n):
    return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))

    
j=int(raw_input().strip())
for x in xrange(j):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    #res=findTrac([0,0],n,k)
    res=factTrac(n,k)
    if res>(pow(10,9)+7):
        print res%(pow(10,9)+7)
    else:
        print res
