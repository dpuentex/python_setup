#HW 2
#Question 1
#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    
    return max(num1, num2, num3)

num1 = 10
num2 = 30
num3 = 15

print("Max Number", max_num(num1, num2, num3))

# Question 2
#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [2, 3, 4, 5]

print(mult_list(numbers))

# Question 3
#Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return ''.join(reversed(string))

string = "HhhhhhhEEEEEEYYYYYYY"
print(rev_string(string))


#Question 3 
#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(number, start, end):
    return start <= number <= end

start_range = 10
end_range = 20
num = 15

if num_within(num, start_range,end_range):
    print(f"{num} falls within [{start_range}, {end_range}]")
else:
    print(f"{num} does not fall withing the range [{start_range}, {end_range}]")