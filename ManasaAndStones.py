'''
Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either  or . Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was , find all the possible values for the number on the last stone.

Note: The numbers on the stones are in increasing order.

Input Format

The first line contains an integer , i.e. the number of test cases.  test cases follow; each has 3 lines. The first line contains  (the number of stones). The second line contains , and the third line contains .

Constraints

Output Format

Space-separated list of numbers which are the possible values of the last stone in increasing order.

Sample Input

2
3 
1
2
4
10
100
Sample Output

2 3 4 
30 120 210 300 
Explanation

All possible series for the first test case are given below:

0,1,2
0,1,3
0,2,3
0,2,4
Hence the answer 2 3 4.

Series with different number of final steps for second test case are the following:

0, 10, 20, 30
0, 10, 20, 120
0, 10, 110, 120
0, 10, 110, 210
0, 100, 110, 120
0, 100, 110, 210
0, 100, 200, 210
0, 100, 200, 300
Hence the answer 30 120 210 300.
'''

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())
    finalStage=[]
    if b>a:
        a,b=b,a
    if a!=b:
        for x in xrange(n):
            finalStage.append(a*x + b*(n-1-x))
    else:
        finalStage.append(a*(n-1))
    print ' '.join(map(str,finalStage))
