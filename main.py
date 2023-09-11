
"""var_toto="toto"
var_num=10
var_toto=var_toto[::-1]

var_num=(str(var_num)[::-1])

print(var_toto)
print(var_num)"""



"""""
def adder (list,num=2):
    i=0
    for i in range(0,(2*len(list)-1)):
        if i%2!=0:
            list.insert(i,num)
    i=i+1



first_list=[1,0,2]
lenght_list=len(first_list)
number_to_ad=int(input("Enter the number that you want to concatenate to the list\nNumber:"))
adder(first_list,number_to_ad)
print("The list concatenated with the number of:", number_to_ad,"\nModified list:",first_list)


"""

"""
def concatenate_list (lst,num):
    lst=num*lst
    return lst

first_list=[1,0,2]

while True:
    number_to_add = input("Enter an integer to concatenate the list (press Enter to use default value)\nNumber:")
    if number_to_add=="":
        print("There is no value for the number of concetanation\nDefault number is: 2:")
        number_to_add="2"
        break
    else:
        break
first_list=concatenate_list(first_list,int(number_to_add))
print(first_list)

i=0
while i<len(third_list):
    if third_list[i]!=None:
        print(third_list[i])
        i+=1
    else:
         break
"""""

first_list=[1,3,2,7,4,10,46,47,41]
print(first_list[:3])
second_list=first_list[2:5]
print(second_list)
third_list=first_list+second_list
print(third_list)
tuple_of_list= zip(first_list,second_list)
print(list(tuple_of_list))
first_list.append(5)

""""
third_list.append(None)
print(third_list)
def nof_even_calculator(lst):
    count_even=0
    for i in lst:
        if i%2==1:
            count_even+=1
    return count_even"""

"""nof_even=nof_even_calculator(first_list)
print(nof_even)""""""

even_numbers = [element for element in first_list if element % 2 == 0]
print(even_numbers)

even_numbers=[]
for element in first_list:
    if element%2==0:
        even_numbers.append(element)

print(even_numbers)"""
def str_to_first_letter(s):
    return s[0]

my_string="Macit"
first_letter=str_to_first_letter(my_string)
print(first_letter)