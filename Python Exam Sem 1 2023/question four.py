
# i

aa =1
bb =2
cc= 3
dd =4
ee= 5
print(aa)
print(aa,bb)
print(aa,bb,cc)
print(aa,bb,cc,dd)
print(aa,bb,cc,dd,ee)


# ii


# iii

a,b =3,4
numbers = a + b
def sum_up_numbers(numbers):
    null_number = 0
    for x in numbers:
        null_number +=x
    return numbers

print(numbers)


# iv

class Car:

    def __init__(self, brand, year):

        self.brand = brand
        self.year = year

car_one = Car('Jeep', '2020')
print(car_one.brand)
print(car_one.year)


# v

car_two =Car('Hilux', '2023')
print(car_two.brand)
print(car_two.year)

