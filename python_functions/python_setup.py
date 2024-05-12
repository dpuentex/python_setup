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