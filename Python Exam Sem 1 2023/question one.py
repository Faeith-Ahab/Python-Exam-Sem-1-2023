# i

def calculate_area(radius):
    pi= 3.14
    return pi * radius
print(calculate_area(2))
print(calculate_area(5))


# ii


# iii

numbers =[1,3,5,7,9]
numbers_edited = numbers.pop(2)
print(numbers)
numbers.insert(4, 10)
print(numbers)


# iv

numbers= [2,4,6,8,10]
the_even_numbers =[num for num in numbers if num % 2 == 0]
print("The even numbers are;", the_even_numbers)


# v

student_info = {'name': 'Alice', 'age':20, 'grade':'A'}
print(student_info)

student_info.update({'age': 25})
print(student_info)


# vi

dict = {'a':3, 'b':8, 'c':2, 'd':7}
new_dict =[8,7]
print("The numbers greater than five are;", new_dict)

