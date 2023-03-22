# prime numbers

lower_value = int(input("Enter the lowest range value:"))
upper_value = int(input("Enter the upper range value:"))

print("The prime numbers in the range are:")
# prime numbers are greater than one
for number in range (lower_value, upper_value + 1):
    if number>1:
        for i in range (2, number):
            if(number % i)==0:
                break
        else:

          print(number)







