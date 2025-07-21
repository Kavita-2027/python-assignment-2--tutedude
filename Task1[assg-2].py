num=int(input('Enter a number:\t'))
if num%2==0:
    num=str(num)
    print(f'{num} is an even number.') #f"{num}" stands for formatted string in python
else:
    num=str(num)
    print(f"{num} is an odd number.")