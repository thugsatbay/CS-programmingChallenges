def print_abacus(value):

    #x=9
    #while(x>=0):
        #cnt=(int)(value/pow(10,x))
        #print ("|"+("0"*(5-(cnt%5)))+("   "*(int)(cnt/5))+("0"*(cnt%5))+(("*")*(5-(cnt%5)))+(("   ")*(1-(int)(cnt/5)))+(("*")*((cnt%5)))+"|")
        #value-=cnt*pow(10,x)
        #x-=1

    for x in range(0,10):
        cnt=(int)(value/pow(10,9-x))
        print ("|"+("0"*(5-(cnt%5)))+("   "*(int)(cnt/5))+("0"*(cnt%5))+(("*")*(5-(cnt%5)))+(("   ")*(1-(int)(cnt/5)))+(("*")*((cnt%5)))+"|")
        value-=cnt*pow(10,9-x)
        


###  TEST CASES
print ("Abacus showing 0:")
print_abacus(0)

#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print ("Abacus showing 12345678:")
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print ("Abacus showing 1337:")
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
