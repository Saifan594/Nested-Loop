print( "\033c" )

num = int(input( "enter a number : " ))

if num == 0 or num == 1:
    print( f"{num} is not a prime number" )

elif num > 1:
    
    for i in range (2, num):
        
        if num % i == 0:
            
            print( f"{num} is not a prime number" )
            print( f"{i} times {num // i} is {num}" )
            
            break
    
    else:
        
        print( f"{num} is a prime number" )

else:
    print( f"{num} is not a prime number" )