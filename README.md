# Python
Code Related to python progamming


Installed folder location:
C:\Users\ssalman\AppData\Local\Programs\Python\Python310


https://statinfer.com/104-1-1-introduction-to-python-and-ide-for-python/
104.1.1.Introduction to Python and IDE for Python

>py -m pip --version

https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html

Importing pandas to python
Enter the command “pip install pandas” on the terminal. This should launch the pip installer. 
The required files will be downloaded, and Pandas will be ready to run on your computer.
After the installation is complete, you will be able to use Pandas in your Python programs


import pandas as pd
print(pd.__version__)

working fine when checked from cmd

but in IntelliJ getting below error
no module named pandas util in intellij

so goto python packages from bottom menu
search for pandas and click install
this will fix the above issue

chapter 1: variables
name ="Salman"
Age=32

print(name + str(Age))
print(name + " is " +str(Age) +" old")
print("{} is {} old".format(name,Age))
print("%s is %s years old" % (name,Age))
print(f'{name} is {Age} years old')


chapter 2: Functions
Parts of a Function
On every function, we have the letters def, a unique function name, the parenthesis and the colon

example:
def addition():

input() function to read from console
int() -> converts data to integer


chpater 3
arg, Kwargs
def user_info(name, age=0, city='MYS'):
    '''
    We are giving default values to the arg if in case they are not passed while calling.
    These values will be used
    '''
    print("{} is {} years old, from {}".format(name, age, city))
	
user_info('Salman', 32, 'SKP')        # this is positional arguments
user_info('Sam')            # calling function without all args

user_info(age=50, name='SMS', city='BLR')  # this is keyword argument, position does not matter

*arg, **kwargs
The *args allows a function to take any number of positional arguments
def add(*args):
    print(sum(args))


add(2,4)
add(1,2,3,4,5,6,7,8,9)


The **kwargs allows a function to take any number of keyword arguments.
def application(**kwargs):
    print(kwargs)

application(name='Salman', age =32, surname='Shaik', city="SKP")

chapter 4: conditional operators
comparison operators
<,>,<=,>=,!=

control structures
if , elif, else

chapter 5 loops
for loop
fruits = ["apple","banana","orange","pears"]

for fruit in fruits:
    print("would you eat {} ?".format(fruit))

fruits[1]="lemon"
for fruit in fruits:
    print("would you eat {} ?".format(fruit))
	
	
for number in range(1,11):			-- inbuilt function for start and end-1
    print(number)
	
while (condition):
	statement
	loop control

Loop control
Break : end loop goto next stament outside loop
Continue : skip current and goto next part of the loop
Pass: skips any part of code where pass appears


while on:
will keep happening till its off
	on =False

chapter 6: list
python list is collection of items
mutable (add, delete)

variable = [,,,,]

method to work with list
append

eg: fruits = ["peaches","pears","apples"]
fruits.append("Oranges")	-- adding single item at end o flist
fruits.extend(years) -- adding another list to first list

fruits.remove("oranges") -- using exaact name of member

fruits.pop(0) u-- using index position

numbers.sort() -- works with same like data type
print("pears" in fruits)  -- gives True or False
print(fruits.count(1993)) -- number of times member in list
fruits.pop(fruits.index(1993))

chapter 7: dictionaries
key value pairings
mutable : can be changed
syntax: created using {key : value, key:value}
 
methods
get(key)  -- to get value of key
items() -output the key value pairs
keys() accepts whole dictionary and returns the keys
popitem() - removes last item from disctionary