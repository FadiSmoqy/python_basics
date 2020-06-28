users = ["fadi", "ghazi", "ismail", "ido"] # wenn man print ussers schreibt und noch ein zahl und noch das [] dazu dann komm ein name raus der an der stellle ist 
print(users)

gamers = ["fadi","ismail", "ghazi"]
print(gamers[2])


numbers = [1, 33, 76, 5]
print(numbers)
print(len(numbers)) # the value of the numbers

num = [1, 5, 77, 17, 56]
del num[2:] #del deletes the numbers after the number that you have given
print(num)


nums = [1, 6, 77, 84, 93, 3]

del nums[2] #it will delete the number in the place where the number you have given
print(nums)

nums.append(1) #add a number
print(nums)

nums.extend([11, 44, 5, 1]) #add more numbers (viele nummern adden)
print(nums)



numberss = [12, 11, 4, 5, 65, 77, 19, 45]
print(min(numberss)) # shows the smallest number
print(max(numberss)) # shows the bigest number
print(sum(numberss)) # calculates everything together and indicates the solution (indicates the solution = gibt die lösung an)
numberss.sort()# it shows the small number up to the large (zeigt klein bis groß)
print(numberss)








