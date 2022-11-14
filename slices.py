list1 = [1, 2, 3, 4, 5]
list2 = list1[0:3]
print(list2)
list3 = list1[3:len(list1)]
print(list3)
list4 = list2 + list3
print("is list4 the same as list one", list1 ==list4)

strHello = "hello, world!"
substr = strHello[0:5]
print(substr)
print(strHello[-1])