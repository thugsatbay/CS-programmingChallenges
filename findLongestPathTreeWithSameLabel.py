'''
A=[1,1,1,2,2] 
A consists of labels for each nodes in the tree

B=[1,2,1,3,2,4,2,5]
B consists of connections between 2 nodes B[2*i] and B[2*i + 1] 
are nodes connected by edge

Problem:
Find the longest path (edges) in the tree with the same label

        [1](1)
        / \  
   (1)[2] [3](1)
      /     \
  (2[4]     [5](2)
  
For the A,B list the above tree is constructed.
The longest path is 2->3->1 (1), with 1 as the label. Output is 2
'''

A=[1,1,1,2,2]
B=[1,2,1,3,2,4,2,5]
def list_longest_path(root, max_v):
    if not root:
        return None,0

    label_l,count_l=list_longest_path(root.gleft(), max_v)
    label_r,count_r=list_longest_path(root.gright(), max_v)
    #print root.getVal(),label_l,count_l, label_r,count_r,max_v
    if label_l and label_r:
        if label_l==label_r:
            if root.getVal() == label_l:
                return label_l, count_l+count_r+2
            max_v[0] = max(max_v[0], count_l, count_r)
            return root.getVal(), 0
        else:
            if label_l==root.getVal():
                return label_l, count_l+1
            elif label_r==root.getVal():
                return label_r, count_r+1
            max_v[0] = max(max_v[0], count_l, count_r)
            return root.getVal(), 0
    elif label_l:
        if label_l==root.getVal():
            return label_l, count_l+1
        max_v[0] = max(max_v[0], count_l)
        return root.getVal(), 0
    elif label_r:
        if label_r==root.getVal():
            return label_r, count_r+1
        max_v[0] = max(max_v[0], count_r)
        return root.getVal(), 0
    else:
        return root.getVal(), 0

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def leftExist(self):
        return self.left

    def rightExist(self):
        return self.right

    def setLeft(self, val):
        self.left = val

    def setRight(self, val):
        self.right = val

    def getVal(self):
        return self.val

    def gleft(self):
        return self.left
    
    def gright(self):
        return self.right

def fun(A, E):
    dic_e = {}
    for ind,ele in enumerate(A):
        dic_e[ind+1] = Node(ele)
    
    for ind in xrange(0,len(B)-1, 2):
        if not dic_e[B[ind]].leftExist():
            dic_e[B[ind]].setLeft(dic_e[B[ind+1]])
        else:
            dic_e[B[ind]].setRight(dic_e[B[ind+1]])
    max_v=[0]
    a,b=list_longest_path(dic_e[1],max_v)
    return max(max_v[0], b)
    #print max_v

print fun(A,B)




def repeatedStringMatch(A, B):
    q = (len(B) - 1) // len(A) + 1
    print q
    for i in range(2):
        if B in A * (q+i): return q+i
    return -1

repeatedStringMatch("abcd","cdabcdab")
