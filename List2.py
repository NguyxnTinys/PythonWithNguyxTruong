number = [1, 2, 3, 4, 5]

#[1] append
# A.append(x) add x to the end of list A
number.append(6) #res = [1, 2, 3, 4, 5, 6]

#[2] insert
# number.insert(index, object)
number.insert(0, 7) #res == [7, 1, 2, 3, 4, 5, 6]

#[3] remove
# number.remove(object)
x = int(input("Remove number: "))
if x in number:
    number.remove(x)

#[4] clear
# number.clear() #res = []

#[5] Length
# len(list)
print("Lenngth of list: ", len(number))

print("Element in the list: ", number)