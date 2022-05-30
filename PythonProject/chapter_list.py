fruits =["apples","pears","banana"]
year = [2,1993,2020,"1998"]

print(fruits)
print(year)

fruits.append("Oranges")
print(fruits)

fruits.extend(year)
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop(0)
print(fruits)

numbers =[8,5,3,9,6,2]
numbers.sort()
print(numbers)

print("pears" in fruits)
print(fruits.count(1993))
print(fruits.count("1993"))
fruits.pop(fruits.index(1993))
print(fruits)