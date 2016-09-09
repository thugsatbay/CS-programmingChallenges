# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If the first number in the string is greater than or equal 
# to the proceeding number, the proceeding number should be inserted 
# into a sublist. Continue adding to the sublist until the proceeding number 
# is greater than the first number before the sublist. 
# Then add this bigger number to the normal list.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    # YOUR CODE
    main_lst,sub_list,grt,x=[],[],0,0
    while(x<len(string)):
        if(int(string[x])>=grt): #line can be removed redundant
            main_lst.append(int(string[x]))
            grt=int(string[x])
            k=x+1
            while (k<len(string)):       
                if(int(string[k])<=grt):
                    sub_list.append(int(string[k]))
                else:
                    grt=int(string[k])
                    #print grt,k
                    break
                k+=1
            x=k-1
            #print x
            if(sub_list):
                main_lst.append(sub_list)
            sub_list=[]
        x+=1
    return main_lst

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result,
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
