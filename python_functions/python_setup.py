# Funcition 1
def hello():
    print('hello world')

hello()


#Function 2
def pack(a, b, c,):
    return[a, b, c]

fruit = pack("Apple", 'Banana', "Orange")
print(fruit)

#Function 3

def eat_lunch(food_list):
    if not food_list:
        print("My lunch box is empty!!")
    else:
        print("First I eat my", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

                        
food_list = ['sandwich', "chips", "apples"]
eat_lunch(food_list)


#FUNCTION ACTIVITY 2

#function 1

def arb_args(*args):
    for arg in args:
        print(arg)

arb_args(1, "hey", [1, 2, 3], {'a': 1, 'b': 2})

#function 2
def inner_func(a, b):

 def opp_1(x, y):
  return x + y

 def opp_2(x, y):
  return x * y
    
 res_1 = opp_1(a, b)
 res_2 = opp_2(a, b)
 total = res_1 + res_2

 print ("Results of opp_1 ", res_1)
 print ("results of opp_2", res_2)
 print ("Total result:", total)

inner_func(4, 7)

# function 3







            
