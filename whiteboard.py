#write a function that doubles every second integer in a list starting from the left.

def double_every_other(numbers):
    for n in range(1,len(numbers),2):
       numbers[n] = (numbers[n]) * 2
    return numbers
my_list = [1, 2, 3, 4]       
print(double_every_other(my_list))