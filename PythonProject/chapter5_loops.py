#for loop
fruits = ["apple","banana","orange","pears"]

for fruit in fruits:
    print("would you eat {} ?".format(fruit))

fruits[1]="lemon"
for fruit in fruits:
    print("would you eat {} ?".format(fruit))

for number in range(1,11):
    print(number)

for number in range(1,11):
    if number == 7:
        print("we are skipping {}".format(number))
        continue
    print("The Number is {}".format(number))

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The Number is {}".format(number))