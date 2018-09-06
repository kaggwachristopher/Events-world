odd=[]
even=[]
def number_game(x,y):
       
    if (y<x):
        if even!=[]:
            even.clear()
            for number in range(y,x):
                if (number%2==0):
                    even.append(number)
            return(even)
        
    elif  (x==0 and y==0):
        return[]
    else:
        if odd!=[]:
            odd.clear()
            for number in range(x,y):
                if (number%2!=0):
                    odd.append(number)
            return(odd)
        else:
            for number in range(x,y):
                if (number%2!=0):
                    odd.append(number)
            return(odd)    
'''
[3, 5, 7, 9, 11])
[3, 5, 7, 9, 11]
[]
[180, 182, 184, 186, 188, 190, 192, 194, 196, 198]
[181, 183, 185, 187, 189, 191, 193, 195, 197, 199]
'''
print(number_game(180,200))
print(number_game(2,12))
print(number_game(0,0))

