print("\033c")

# input a number
number=int(input("enter the number : "))
t=number
number_length=0

# iterate the loop
while t>0:
    number_length=number_length+1
    t=int(t/10)

if number_length>=4:    #condition 1
    number_length=int(number_length/2)
    character=0
    while number>0: # iterate loop
        remainder=number%10
        if character==number_length:    # nested condition 1
            middle_one=remainder
        elif character==number_length-1:
            middle_two=remainder
        number=int(number/10)
        character=character+1
    product=middle_one*middle_two   # product of middle digits
    # display the result
    print("\nproduct of middle digits ("+str(middle_one)+"*"+str(middle_two)+") =",product)

else:
    print("\nit is not a 4 or more than 4-digit number!")