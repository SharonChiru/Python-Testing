
def add_nums():
    print(2+13)
add_nums()

#Abitrary Arguments, *args
#if the number of arguments is unknown , add a * before the parameter

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Sharon", "Hope", "Caleb")

def add_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print("Total: ", add_nums (2,5,6,7,8,13))


#Abitrary Key worrds Arguments **kwargs
#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
    print("her last name is " + kid["lname"])
my_function(fname = "Sharon", lname = "Shume")