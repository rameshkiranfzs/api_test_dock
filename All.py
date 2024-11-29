'''Longest Substring without repeating character'''
# def length_of_longest_substring(inpstring):
    
#     dict = {}
#     count = 1
#     str = ""
#     for i in inpstring:
#         if i in dict:
#             dict[i]+=count
#         else:
#             dict[i]=1
#             str+=i
#     print(str)


# length_of_longest_substring("bbbbbc")

'''Longest palindromic Substring '''

# def long_palindromic(instring):
#     maxp=""
#     for i in range(len(instring)):
#         for j in range (i+2, len(instring)):
#             if instring[i:j]==instring[i:j][::-1]:
#                 if len(instring[i:j]) > len(maxp):
#                     maxp= instring[i:j]

#     print(maxp)

# long_palindromic("aamalayalamddugy")

'''Shortest palindromic Substring '''

# def small_palindromic(instring):
#     maxp=instring
#     for i in range(len(instring)):
#         for j in range (i+2, len(instring)):
#             if instring[i:j]==instring[i:j][::-1]:
#                 if len(instring[i:j]) < len(maxp):
#                     maxp= instring[i:j]

#     print(maxp)

# small_palindromic("aamalayalamddugy")

'''Reverse an integer '''

# def reveint(inti):
#     neg = 1
#     if inti<0:
#         neg = -1
    
#     # revint = int(str(abs(inti))[::-1]) * neg
#     revint = int(str(inti * neg)[::-1]) * neg
#     print(revint)

# reveint(-123)

'''Roman To Integer '''
# def roman_to_int(inti):
#     romandict = {
#         "M":1000,
#         "D":500,
#         "C":100,
#         "L":50,
#         "X":10,
#         "V":5,
#         "I":1
#                 }
#     total = 0
#     prev_val = 0
#     for s in inti[::-1]:
#         current_val = romandict[s]
#         if current_val > prev_val:
#             total +=current_val
#         elif current_val < prev_val:
#             total -=current_val
#         else:
#             total +=current_val
        
#         prev_val= current_val
#     print(total)


# roman_to_int('MCMXCIII')

'''Find total from a list '''
# def total_add(list_total):
#     total=0
#     for i in list_total:
#         if isinstance(i,(tuple,list)):
#             total+=total_add(i)
#         if isinstance(i,(int,float)):
#             total+=i
    
#     return total



# print(total_add([1,2,[2,3],(3,4),[(1,[2,4]),[2,3,4]]]))

'''Sort Dictionary'''
'''By Keys'''
# my_dict = {
#     3: 'apple',
#     1: 'banana',
#     4: 'cherry',
#     2: 'date'
# }
# mydict = dict(sorted(my_dict.items()))
# print(mydict)

'''By Values'''
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'grape'}
# mydict_sort = dict(sorted(my_dict.items(),key=lambda x:x[1],reverse=True))
# print(mydict_sort)

'''Convert Number to Roman'''

# def num_to_roman(inti):
#     roman =  [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
#         (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#         (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
#         (1, 'I')]
    
#     roman_numerals = ""

#     for value,symbol in roman:
#         while inti>=value:
#             roman_numerals+=symbol
#             inti-=value
    
#     print(roman_numerals)
# num_to_roman(1992)

'''longest common prefix'''

# inti = ["flower", "flow", "flight"]

# prefix= inti[0]

# for strs in inti[1:]:
#     while not strs.startswith(prefix):
#         prefix = prefix[:-1]

# print(prefix)

'''Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0'''

# inti_list = [0,-1,1,1,-1]

# len_inti  = len(inti_list)
# add_list = []
# for i in range(0,len_inti-2):
#     for j in range(i+1,len_inti-1):
#         for k in range(j+1,len_inti):
#             res = inti_list[i] + inti_list[j] + inti_list[k]

#             if res == 0:
#                 add_list.append([inti_list[i],inti_list[j],inti_list[k]] )

# uniqueset ={ tuple(list1) for list1 in add_list}
# uniquelst = [list(list1) for list1 in uniqueset]
# print(uniquelst)

'''Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.'''
# nums = [-1,2,1,-4]
# target = 1

# closest_sum = 10**100
# lenn = len(nums)
# for i in range(0,lenn):
#     for j in range (i+1,lenn):
#         for  k in range (j+1,lenn):
#             current_sum = nums[i]+nums[j]+nums[k]
#             if abs(current_sum-target) < abs(closest_sum-target):
#                 closest_sum = current_sum

# print(closest_sum)

'''Factorial'''

# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)

# print(fact(5))

'''Fibonacci Series '''

# def fibo(n):
#     if n==1 or n==2:
#         return 1
#     if n ==0:
#         return 0
    
#     return fibo(n-1)+fibo(n-2)

# print(fibo(10))


'''Prime Number'''
# n = 15
# test  =""
# for i in range(2,n-1):
#     if n%i==0:
#         test =  "is not a prime number "
        
#         print(test)
#         break

# print(test)


'''Consecutive numbers'''

# def longest_consecutive(nums):
#     # Step 1: Create a set of the numbers
#     num_set = set(nums)
#     max_length = 0
    
#     # Step 2: Iterate through the numbers
#     for num in num_set:
#         # Check if it's the start of a sequence
#         if num - 1 not in num_set:
#             current_num = num
#             current_length = 1
            
#             # Step 3: Count the length of the sequence
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_length += 1
            
#             # Step 4: Update the maximum length
#             max_length = max(max_length, current_length)
    
#     return max_length

# # Example usage:
# print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4

''' Move zeros to last'''
# nums = [100,0, 4, 200,0, 1, 3, 2,0]
# zerolist = []
# newlist= []
# for n in nums:
#     if n==0:
#         zerolist.append(n)
#     else:
#         newlist.append(n)

# for list in zerolist:
#     newlist.append(list)

# print(newlist)

'''Find the Index of the First Occurrence in a String
'''
'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''

# haystack = "qqqsadbutsad" 
# needle = "sad"

# for i in range(len(haystack)):
#     for j in range(i,len(haystack)):
#         if haystack[i:j+1]==needle:
#             print(i)

'''generate a list of length 5 where the sum of the elements is 0'''
# import random
# numlist = [random.randint(-10,10) for s in range(0,4)]
# resultnum = -sum(numlist)

# numlist.append(resultnum)
# print(numlist)


''' A phrase is a palindrome if,
 after converting all uppercase letters into lowercase letters and removing all 
 non-alphanumeric characters,
 it reads the same forward and backward. '''

# s = "A man, a plan, a canal: Panama"
# str1 = "".join([si.lower() for si in s if si.isalnum()])
# if str1 == str1[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrom")


'''Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.'''

# nums = [100,4,200,1,3,2]

# nums= sorted(nums)
# seqlist = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+1 ==nums[j]:
#             seqlist.append(nums[i])
#             seqlist.append(nums[j])

# print(list(set(seqlist) ))

'''get max occuring elements in a list '''
# countdict = {}
# count = 1
# for i in nums:
#     if i in countdict:
#         countdict[i]+=count
#     else:
#         countdict[i]=count

# maxvalue= max(countdict.values())

# value = [key for key,val in countdict.items() if val==maxvalue ]
# print(value)

'''Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.'''

# nums = [10,2]

# nums = "".join(map(str,nums))
# new = sorted(nums,reverse=True)
# nums = "".join(map(str,new))
# print(nums)

'''calculate the 
frequency
 of each word '''

# longstring = "the day is sunny the the the sunny is is"

# longstring = longstring.split(" ")

# countdict = {}
# count = 1
# for i in longstring:
#     if i in countdict:
#         countdict[i]+=count
#     else:
#         countdict[i]=1

# maxvalue= max(countdict.values())

# keyword = [key for key,value in countdict.items() if value==maxvalue]


