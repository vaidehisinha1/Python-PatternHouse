height = int(input())

for i in range(0,height+1):

    for j in range(0,height-i+1):
        print(end=" ")

    for j in range(0,i):
        
        if(i%2 == 0):
            print(j+1,end=" ")

        else:
            c = chr(j+65)
            print(c,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
#      A 
#     1 2 
#    A B C 
#   1 2 3 4 
#  A B C D E 
