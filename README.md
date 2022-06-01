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
setdefault() Retrieves the value for a specific key or add a new key and default value into the dictionary
	stuff.setdefault("friends",123)
update() : update or add any item to list
	stuff.update(rocks=45,stone=7)


chapter 8 : classes
inherirence
multiple inheritence
polymorphism

class variables
instant variable


__init__ method

1. What is a class?
A way to group related functions and variables
2. What is a class variable?
A variable that is available to every class method
3. What is an instance variable?
A variable that is only available to a specific method
4. What is __init__?
A method that acts as a constructor, allowing for an object to be created with specific parameters
5. What is self?
Self makes all class methods available to every object that is created by a class
6. What is the proper syntax for a new class?
class New:
7. What is the syntax for the first line of the init method?
def __init__(self, arguments):

-------------------------------------
packages in python

import math  - log(), exp(), sqrt()
import numpy - 			numerical library in Python
	array([])
	loadtxt('convertcsv.csv', delimeter = ',')
	
import requests - get(http path)
import pandas - read_csv(file path / variable), set_option('display.max.columns',None) ('display.precision',2)

with open('nbaallelo.csv', 'wb') as f:
    f.write(response.content)
	
The dataset that we are going to use to load data can be found here. It is named as 100-Sales-Records.
https://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/

reading file manually using function
def load_csv(filepath):
    data =  []
    col = []
    checkcol = False
	with open(filepath) as f:					-- opening file using path
    for val in f.readlines():				-- reading each line in iterator
        val = val.replace("\n","")			-- to replace charachter in line
        val = val.split(',')				-- csv file spliting by ,
		if checkcol is False:
                col = val
                checkcol = True
            else:
                data.append(val)			-- adding each lines to list
    df = pd.DataFrame(data=data, columns=col)
    return df

numpy package
file2 = np.loadtxt(fname="C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\test2.txt",delimiter='|')
 It is very useful for reading data which is of the same datatype.
 
file3 = np.genfromtxt(fname="C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\100-Sales-Records\\100 Sales Records.csv",delimiter=',', dtype=None, names=True, encoding='utf-8')
to read any datatye

pd.DataFrame(file3) to ready as dataframe

import pickle
When your data is not in a good, human-readable format, you can use pickle to save it in a binary format. 
Then you can easily reload it using the pickle library.