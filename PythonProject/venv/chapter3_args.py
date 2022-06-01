def user_info(name, age=0, city='MYS'):
    '''
    We are giving default values to the arg if in case they are not passed while calling.
    These values will be used
    '''
    print("{} is {} years old, from {}".format(name, age, city))


user_info('Salman', 32, 'SKP')        # this is positional arguments
user_info('Sam')            # calling function without all args

user_info(age=50, name='SMS', city='BLR')  # this is keyword argument, position does not matter


# The *args allows a function to take any number of positional arguments.
def add(*args):
    print(sum(args))


add(2,4)
add(1,2,3,4,5,6,7,8,9)


# The **kwargs allows a function to take any number of keyword arguments

def application(**kwargs):
    print(kwargs)

application(name='Salman', age =32, surname='Shaik', city="SKP")

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email),args,kwargs)

application("Jess", "Ingrass", "email@mail.com", "Teach Code", 75000, hire_date = "September 2010")