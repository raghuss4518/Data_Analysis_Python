numbers = [1,2,3,4,5,6,7,8,9,10] 
list_odd_num = []

for num in numbers:
    if num % 2 != 0:
        list_odd_num.append(num)
        print(num)
        