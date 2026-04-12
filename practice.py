
# # # Factorial using recursion
# # def fact(no):
# #     if no==0 or no==1: 
# #         return 1
# #     return no * fact (no-1)
# # no = 4
# # print(fact(no))

# # # from a list find the second largest number
# # def secondHigh(no):
# #     if len(no) == 1:
# #         return no[0]
# #     num = list(set(no))
# #     num.sort()
# #     return num[-2]

# # no = [1,2,3,4,1,2,3,2,4,5,6]
# # print(secondHigh(no))

# # from a list of strings find the strings which are palindrom

# # def palin(p):
# #     new_list=[]
# #     for i in p:
# #         new_s=i
# #         if i==new_s[-1::-1]:
# #             new_list.append(i)

# #     return new_list

# # p = ['madam','hello', 'noon','python','level','1221']
# # print(palin(p))
# # palindromes = [word for word in p if word == word[::-1]]
# # print(palindromes)  


# #Anagram
# # def ana(w1,w2):
# #     w1 = w1.lower().replace(" ","")
# #     w2 = w2.lower().replace(" ","")
# #     if sorted(w1) == sorted(w2):
# #         return ' Anagram'
# #     else:
# #         return 'Not Anagram'
# # w1 = 'Dormitoryw'
# # w2 = 'Dirty Room'
# # print(ana(w1,w2))
# # def has_anagram(word_list):
# #     seen = set()   # store sorted versions

# #     for word in word_list:
# #         clean = word.lower().replace(" ", "")
# #         sorted_word = "".join(sorted(clean))

# #         if sorted_word in seen:
# #             return True   # anagram mil gaya

# #         seen.add(sorted_word)

# #     return False  # koi anagram nahi mila


# # # Example
# # words = ['listen', 'hello', 'race', 'care', 'world']
# # print(has_anagram(words))


# # 30questions
# ##reverse a string

# # def reverse_str(s):
# #     new_s = ""
# #     for i in s[::-1]:
# #         new_s = new_s+i
# #     return new_s
# # s="qwerty"
# # print(reverse_str(s))


# # s='qwerty'
# # print(s[::-1])

# # check whether a string is palindorme or not
# # s='madam'
# # palin = s[::-1]
# # if(s==palin):
# #     print("YES")
# # else:
# #     print("NO")

# ## using two pointers
# # def check_palin(s):
# #     left = 0 
# #     right = len(s)-1
# #     while(left<right):
# #         if s[left]!=s[right]:
# #             return False
# #         left = left+1
# #         right = right-1

# #     return True
# # s="madam"
# # print(check_palin(s))

# # count vowels and consonants + if a str contains any character
# # def countV(s):
# #     for ch in s:
# #         if ch< '0' or ch >'9':
# #             return False
# #     return True

# # s='123r'
# # print(countV(s))
    

# #     vowel=0 
# #     c=0
# #     for i in s:
# #         if i.isalpha():
# #             if i.lower() in ['a','e','i','o','u']:
# #                 vowel+=1
# #             else:
# #                 c +=1
# #     print("Vowel = ", vowel, "Consonant = ",c)
# # s="Hello World"
# # countV(s)

# # Swap cases of a character in a string
# # def swapC(s):
# #     new_s=''
# #     for i in s:
# #         if i.islower():
# #             new_s=new_s+i.upper()
# #         elif i.isupper():
# #             new_s=new_s+i.lower()
# #         else:
# #             new_s=new_s+i
        
# #     print(new_s)

# # s="Hello World"
# # swapC(s)

# # def str_to_charA(s):
# #     char_arr = []
# #     for ch in s:
# #         char_arr.append(ch)
# #     print("char array: ",char_arr)
# #     result =""
# #     for ch in char_arr:
# #         result+=ch
# #     print("back to str " , result)

# # s="hello"
# # str_to_charA(s)

# ##remove punctuations from a string
# # def remp(s):
# #     new_s=''
# #     for i in s:
# #         if i.isalpha() or i.isdigit() or i==' ':
# #             new_s=new_s+i
# #     return new_s    
# # s="Hello, World! how are you?"
# # print(remp(s))

# # count no of words in a string
# # def countWord(s) -> int:
# #     count = 0
# #     in_word = False

# #     for ch in s:
# #         if ch != ' ':
# #             if not in_word:
# #                 count += 1
# #                 in_word = True
# #         else:
# #             in_word = False

# #     return count


# # s = "Hello World, How are you? are you doing well? i can't believe it's been that long."
# # print(countWord(s))

# # def validate_number(s):
# #     if not s:
# #         return "Invalid"

# #     # handle negative
# #     if s[0] == '-':
# #         s = s[1:]

# #     if not s:
# #         return "Invalid"

# #     dot_count = s.count('.')

# #     if dot_count == 0:
# #         # Integer check
# #         for ch in s:
# #             if ch < '0' or ch > '9':
# #                 return "Invalid"
# #         return "Integer"

# #     elif dot_count == 1:
# #         # Float check
# #         left, right = s.split('.')

# #         if left == "" or right == "":
# #             return "Invalid"

# #         if not left.isdigit() or not right.isdigit():
# #             return "Invalid"

# #         return "Float"

# #     else:
# #         return "Invalid"

# #validate email address
# # def validEmail(s):
# #     if '@' not in s:
# #         return False
# #     if s.count('@')!=1:
# #         return False
# #     at_pos = s.index('@')

# #     if at_pos ==0 or at_pos == len(s)-1:
# #         return False
    
# #     if'.' not in s[at_pos:]:
# #         return False
# #     if s.endswith('.'):
# #         return False
# #     return True

# # s =[
# #     "abc@gmail.com",
# #     "abc@gmail",
# #     "@gmail.com",
# #     "abc@gmail.",
# #     "abc@@gmail.com"
# #  ]

# # for e in s :
# #     print(e,"->", validEmail(e))


# # def extractNo(s):
# #     curr = ""
# #     new_list = []
# #     for i in s:
# #         if i.isdigit():
# #             curr = curr + i
# #         else:
# #             if curr != "":
# #                 new_list.append(int(curr))
# #             curr = ""
# #     if curr != "":
# #         new_list.append(int(curr))
# #     return new_list

# # stri = "a12b34c5"
# # print(extractNo(stri))

# #convert string to camel Case
# # def camel_case(s):
# #     new_s=""
# #     cap_next = False
# #     for i in s:
# #         if i== " " or i=="_" or i=="-":
# #             cap_next=True
# #         else:
# #             if cap_next:
# #                 new_s += i.upper()
# #                 cap_next = False
# #             else:
# #                 new_s += i.lower()
# #     return new_s

# # print(camel_case("hello world program"))
# # print(camel_case("convert_to_camel case"))


# # count frequency of each character in a string
# # def countFreq(s):
# #     new_dict = {}
# #     for i in s:
# #         if i in new_dict:
# #             new_dict[i]+=1
# #         else:
# #             new_dict[i]=1
# #     return new_dict

# # print(countFreq("aabbbdee"))

# #count first non repeating character in a string
# # def countNonR(s):
# #     new_dict={}
# #     for i in s:
# #         if i in new_dict:
# #             new_dict[i] +=1
# #         else:
# #             new_dict[i]=1
# #     for i in new_dict:
# #         if new_dict[i]==1:
# #             return i
# #     return None
    
# # print(countNonR("aabbccde"))
            

# # check if an string is an isogram
# #isogram wo hote jinme repeating character ni hota

# # def isogram(s):
# #     return len(set(s))==len(s)

# # print(isogram('Machine'))
# # print(isogram('Hello'))
# # print("\n-----------\n")
# # def is_iso(s):
# #     new_set = set()
# #     for i in s:
# #         if i in new_set:
# #             return False
# #         new_set.add(i)
# #     return True

# # print(is_iso('Machine'))
# # print(is_iso('Hello'))


# #Longest substring without non repeating characters
# # def longSubstr(s):
# #     left=0, max_length=0
# #     newSet= set()
# #     for i in range(len(s)):
# #         while s[i] in newSet:
# #             newSet.remove(s[left])
# #             left=left+1
# #         newSet.add(s[i])
# #         max_length=max(max_length, i-left+1)
# #     return max_length

# # print(longSubstr("abcabcbb"))  # 3
# # print(longSubstr("bbbbb"))     # 1
# # print(longSubstr("pwwkew"))    # 3

# #check if one string is a subsequence of another
# # def subseq(s1,s2):
# #     i=0
# #     j=0
# #     while i<len(s1) and j<len(s2):
# #         if s1[i]==s2[j]:
# #             i+=1
# #         j+=1
# #     return i == len(s1)

# # print(subseq("abc","aXwbfYc"))

# # Phase 4 - String Compression

# # def comp_str (s):
# #     if not s:
# #         return ""
    
# #     result = ""
# #     count = 1

# #     for i in range(1,len(s)):
# #         if s[i]==s[i-1]:
# #             count+=1
# #         else:
# #             result += s[i-1] + str (count)
# #             count = 1

# #     result += s[-1]+str(count)

# #     return result


# # print(comp_str("aaabbc"))
# # print(comp_str("abcd"))
# # print(comp_str("aaaaaavvv"))

# # def substr(s, sub):
# #     i=0
# #     count=0
# #     while i <= len(s) - len(sub):
# #         if s[i:i+len(sub)] == sub:
# #             i = i+len(sub)
# #             count = count+1
# #         else:
# #             i=i+1
# #     return count

# # print(substr("abababa","aba"))

# #replcce a substring with a new substring in a string
# # def newsub(s,o,n):
# #     i=0
# #     result=""
# #     while i <= len(s)-len(o):
# #         if s[i:i+len(o)] == o:
# #             result += n
# #             i+= len(o)
# #         else:
# #             result += s[i]
# #             i+=1

# #     result += s[i:]
# #     return result

# # print(newsub("hello world","world","python"))

# #extract substring between the characters

# # def substrbw(s,start,end):
# #     cs=-1
# #     ce=-1
# #     for i in range(len(s)):
# #         if s[i] == start and cs==-1:
# #             cs=i
# #         elif s[i] == end and ce==-1: 
# #             ce=i
# #             break
# #     if cs==-1 or ce==-1 or ce<cs:
# #         return ""
# #     res= s[cs:ce+1]
# #     return res

# # print(substrbw("abc[d]e","[","]"))

# # check whether a string is a rotation of another string or not
# # def is_rotation(s1,s2):
# #     if len(s1)!=len(s2):
# #         return False
# #     return s2 in (s1+s1)

# # print(is_rotation("abcd","cdab"))

# #compare two string without using .equals()
# # def compstr(s1,s2):
# #     if len(s1)!=len(s2):
# #         return False
# #     for i in range(len(s1)):
# #         if s1[i]!=s2[i]:
# #             return False
# #     return True

# # print(compstr("hi","hil"))

# # find position of a substring in a string
# # def poss(s1,s2):
# #     i=0
# #     while i <= len(s1)-len(s2):
# #         if s1[i:i+len(s2)]==s2:
# #             return i
# #         i+=1
# #     return -1

# # print(poss("hello world","world"))

# # find all unique character in a string

# # def unichar(s1):
# #     i=0
# #     freq={}
# #     for i in s1:
# #         if i in freq:
# #             freq[i]+=1
# #         else:
# #             freq[i]=1
# #     result =""
# #     for i in s1:
# #         if freq[i]==1:
# #             result = result+i
# #     return result

# # print(unichar("aabbccdef"))

# #rotate a string left by k characters
# # def rotatestr(s1,k):
# #     k=k%len(s1)
# #     left=s1[0:k]
# #     right=s1[k:]
# #     return right+left


# # print(rotatestr("abcd",6))

# #Merge two strings alternately

# # def mergeStr(s1,s2):
# #     res=""
# #     i=0
# #     j=0
# #     while i< len(s1) and j<len(s2):
# #         res=res+s1[i]+s2[j]
# #         i+=1
# #         j+=1

# #     while i<len(s1):
# #         res=res+s1[i]
# #         i+=1

# #     while j<len(s2):
# #         res=res+s2[j]
# #         j+=1

# #     return res

# # print(mergeStr("abc","pqrst"))

# # permutations of stirng
# # def perm(s1):
# #     if len(s1)==1:
# #         return [s1]

# #     res = []
# #     for i in range(len(s1)):
# #         fixed = s1[i]
# #         remaining = s1[:i]+s1[i+1:]
# #         for j in perm(remaining):
# #             res.append(fixed+j)
        
# #     return res


# # print(perm("ac"))

# # edit distance
# # def edit_dist(s1,s2):

# #     if len(s1) ==0:
# #         return len(s2)
# #     if len(s2)==0:
# #         return len(s1)
# #     if s1[-1] == s2[-1]:
# #         return edit_dist(s1[:-1], s2[:-1])
# #     return 1 + min(
# #         edit_dist(s1, s2[:-1]),    # insert
# #         edit_dist(s1[:-1], s2),    # delete
# #         edit_dist(s1[:-1], s2[:-1])# replace
# #     )

# # print(edit_dist("cat", "cut"))   # 1
# # print(edit_dist("kitten", "sitting"))  # 3


# # New Question as per the pattern of DSA
# # a. ARRAY
# #  TWO SUMS
# # def twoSum(nums, target):
# #     for i in range(len(nums)):
# #         for j in range(i + 1, len(nums)):
# #             if nums[i] + nums[j] == target:
# #                 return [i, j]


# # # test cases
# # print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
# # print(twoSum([3, 2, 4], 6))        # [1, 2]
# # print(twoSum([3, 3], 6))           # [0, 1]

# #best time to buy & sell stock
# # def bass(a1):
# #     # buy=a1[0]
# #     # store = 0
# #     # for i in a1:
# #     #     if i<buy:
# #     #         buy=i
# #     #     else:
# #     #         profit = i - buy
# #     #         if profit > store:
# #     #             store = profit
# #     # return store
# #     min_price = float('inf')
# #     max_profit = 0

# #     for i in a1:
# #         min_price = min(min_price, i)
# #         max_profit = max(max_profit, i-min_price)
# #     return max_profit
    

# # print(bass([7,1,5,3,6,4]))

# #maximum subarray
# # def maxSubArray(nums):
# #     current_sum = nums[0]
# #     max_sum = nums[0]

# #     for i in range(1, len(nums)):
# #         current_sum = max(nums[i], current_sum + nums[i])
# #         max_sum = max(max_sum, current_sum)

# #     return max_sum


# # # test cases
# # print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
# # print(maxSubArray([1]))                      # 1
# # print(maxSubArray([5,4,-1,7,8]))              # 23
# # print(maxSubArray([-1,-2,-3,-4]))             # -1

# # n = 5
# # sum = 0

# # for i in range(1, n + 1):
# #     res += i ** 3

# # print(res)

# # n = 11
# # if n <= 1:
# #     print(False)
# # else:
# #     is_prime = True  # Flag variable
# #     for i in range(2, int(n**0.5) + 1):
# #         if n % i == 0:
# #             is_prime = False
# #             break
# #     print(is_prime)

# # function to check if a substring 
# # s[low..high] is a palindrome
# # def checkPal(str, low, high):
# #     while low < high:
# #         if str[low] != str[high]:
# #             return False
# #         low += 1
# #         high -= 1
# #     return True

# # # function to find the longest palindrome substring
# # def getLongestPal(s):
    
# #     n = len(s)

# #     # all substrings of length 1 are palindromes
# #     maxLen = 1
# #     start = 0

# #     # nested loop to mark start and end index
# #     for i in range(n):
# #         for j in range(i, n):

# #             # check if the current substring is 
# #             # a palindrome
# #             if checkPal(s, i, j) and (j - i + 1) > maxLen:
# #                 start = i
# #                 maxLen = j - i + 1

# #     return s[start:start + maxLen]

# # if __name__ == "__main__":
# #     s = "forgeeksskeegfor"
# #     print(getLongestPal(s))

#     #DP

# # def getLongestPal(s):
# #     n = len(s)
# #     dp = [[False] * n for _ in range(n)]
    
# #     # dp[i][j] if the substring from [i to j] is a palindrome or not
# #     start = 0
# #     maxLen = 1
    
# #     # all substrings of length 1 are palindromes
# #     for i in range(n):
# #         dp[i][i] = True
    
# #     # check for substrings of length 2
# #     for i in range(n - 1):
# #         if s[i] == s[i + 1]:
# #             dp[i][i + 1] = True
# #             if maxLen == 1:
# #                 start = i
# #                 maxLen = 2
    
# #     # check for substrings of length 3 and more
# #     for length in range(3, n + 1):
# #         for i in range(n - length + 1):
# #             j = i + length - 1
    
# #             # if s[i] == s[j] then check for [i+1 .. j-1]
# #             if s[i] == s[j] and dp[i + 1][j - 1]:
# #                 dp[i][j] = True
# #                 if length > maxLen:
# #                     start = i
# #                     maxLen = length
    
# #     return s[start:start + maxLen]
        
# # if __name__ == "__main__":
# #     s = "forgeeksskeegfor"
# #     print(getLongestPal(s))


# # time complexity questions
# # a = 0
# # b = 0
# # for i in range(N):
# #   a = a + random()

# # for i in range(M):
# #   b= b + random()

# # def fun(n,m):
# #     for i in range(n):
# #         print(i)
# #     for i in range(m):
# #         print(i)


# # print(fun(1,2))

# # def fun(N,M):
# #     arr=[]
# #     counter=0
# #     for i in range(N):
# #         arr.append(i)
# #     for i in range(M):
# #         counter+=1
# #     print(counter)

# # def function(N,M):
# #   counter=0
# #   for i in range(N):
# #     for j in range(M):
# #         counter+=1
# #     print(counter)

# #     def fun(n,m):
# #     arr=[[0]*m for i in range(n)]
# #     for i in range(n):
# #         for j in range(m):
# #             k=1
# #             while k<n*m:
# #                 k*=2

# # LOGIC BUILDING PROBLEMS

# # 1. check even or odd
# # def evenOdd (num):
# #     if num==0:
# #         return True
# #     if num%2==0:
# #         return "It is even"
# #     else:
# #         return "It is odd"
# # print(evenOdd(int(input())))

# # 2.) Multiplication Table
# # def multiTable(num):
# #     if num==0:
# #         return "Enter some other number"
# #     for i in range(1,11):
# #         print(num ,"*", i, "= ", num * i)

# # multiTable(int(input()))

# # 3.) Program for sum of n natural number
# # def natural(num):
# #     if num == 0:
# #         return 0
# #     res=0
# #     for i in range(1,num+1):
# #         res=res+i

# #     return res
# # print(natural(int(input())))

# # 4.) Program for sum of square of first n natural number
# # def sqNat(num):
# #     if num==0:
# #         return 0
# #     res = 0
# #     for i in range(1,num+1):
# #         res = res + i*i
# #     return res
# # print(sqNat(int(input())))

# # 5.) Swap Two Numbers
# # def swap(a,b):
# #     # c=a
# #     # a=b
# #     # b=c
# #     # return (a,b)

# #     # a= (a*b)
# #     # b= a//b
# #     # a=a//b

# #     # a = a+b
# #     # b = a-b
# #     # a=a-b

# #     a= a ^ b
# #     b= a^b
# #     a=a^b

# #     return a,b
# # print(swap(int(input()), int(input())))

# #6.) find closest to n divisible by m
# # def closestn(n,m):
# #     if m==0:
# #         raise ValueError("Divisor can't be equal to 0")
# #     lower = round(n/m)*m
# #     upper = lower + m if n>=0 else lower - m
# #     if abs(n-lower)<abs(n-upper):
# #         return lower
# #     elif abs(n-lower) > abs(n-upper):
# #         return upper
# #     else:
# #         return lower if abs(lower)>abs(upper) else upper

# # print(closestn(int(input()), int(input())))

# #7.) Dice Problem
# # def oppositeFaceOfDice(n):
# #     if n == 1:
# #         return 6
# #     elif n == 2:
# #         return 5
# #     elif n == 3:
# #         return 4
# #     elif n == 4:
# #         return 3
# #     elif n == 5:
# #         return 2
# #     else:
# #         return 1

# # n = int(input())
# # print(oppositeFaceOfDice(n))

# # def nthTermOfAP(a1, a2, n):
# #     nthTerm = a1
# #     d = a2 - a1
# #     for i in range(1, n):
# #         nthTerm += d
# #     return nthTerm


# # a1 = 2
# # a2 = 3
# # n = 4
# # print(nthTermOfAP(a1, a2, n))

# # def nthTermOfAP(a1, a2, n):
# #     # using formula to find the
# #     # Nth term t(n) = a(1) + (n-1)*d
# #     return a1 + (n - 1) * (a2 - a1)


# # a1 = 2
# # a2 = 3
# # n = 4
# # print(nthTermOfAP(a1, a2, n))

# ## reverse digits of a number
# # def rev(no):
# #     res=0
# #     while(no>0):
# #         a=no%10
# #         res=res*10+a
# #         no=no//10
# #     return res

# # print(rev(4562))

# #prime Testing

# # def isPrime(n):

# #     # Corner case
# #     if n <= 1:
# #         return False

# #     # Check from 2 to n-1
# #     for i in range(2, n):
# #         if n % i == 0:
# #             return False

# #     return True


# # # Driver Program to test above function
# # print("true") if isPrime(11) else print("false")
# # print("true") if isPrime(14) else print("false")

# #check if a number is a power of another number
# # def checkPower(x,y):
# #     if x==1:
# #         return y==1
# #     pow=1
# #     while pow < y:
# #         pow *= x
# #     return pow==y
# # print(checkPower(10,11))

# # import math

# # # Function to calculate distance
# # def distance(x1 , y1 , x2 , y2):
# #     return math.sqrt(math.pow(x2 - x1, 2) +
# #                 math.pow(y2 - y1, 2))

# # # Drivers Code
# # print("%.6f"%distance(3, 4, 4, 3))

# # # Python3 program to check if three
# # # sides form a  triangle or not 

# # # function to check if three sides 
# # # form a triangle or not 
# # def checkValidity(a, b, c): 
    
# #     # check condition 
# #     if (a + b <= c) or (a + c <= b) or (b + c <= a) :
# #         return False
# #     else:
# #         return True        

# # # driver code 
# # a = 7
# # b = 10
# # c = 5
# # if checkValidity(a, b, c):
# #     print("Valid") 
# # else:
# #     print("Invalid")


# # # overlapping rectangle
# # class Point:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y

# # def do_overlap(l1, r1, l2, r2):
# #     # If one rectangle is to the left of the other
# #     if l1.x > r2.x or l2.x > r1.x:
# #         return False

# #     # If one rectangle is above the other
# #     if r1.y > l2.y or r2.y > l1.y:
# #         return False

# #     return True

# # # Driver code
# # if __name__ == "__main__":
# #     l1 = Point(0, 10)
# #     r1 = Point(10, 0)
# #     l2 = Point(5, 5)
# #     r2 = Point(15, 0)

# #     if do_overlap(l1, r1, l2, r2):
# #         print("Rectangles Overlap")
# #     else:
# #         print("Rectangles Don't Overlap")

# #factorial
# # def factorial(n):
# #     ans = 1
# #     i = 2
# #     #calculating the factorial
# #     while (i <= n):
# #         ans *= i
# #         i += 1
# #     return ans

# # if __name__ == "__main__":
# #     num = 5
# #     print(factorial(num))


# #pair cube count
# # def count_pairs(n):
# #     count = 0
# #     for a in range(1, n + 1):
# #         for b in range(n + 1):
# #             if a**3 + b**3 == n:
# #                 count += 1
# #     return count

# # n = 9
# # print(count_pairs(n))

# # try:
# #     num1 = int(input('Enter Numerator: '))
# #     num2 = int(input('Enter Denominator: '))
# #     division = num1/num2
# #     print(f'Result is: {division}')
# # except:
# #     print('Invalid input!')
# # else:
# #     print('Division is successful.')


# # ## Try 1 ##
# # # Enter Numerator: 2
# # # Enter Denominator: d
# # # Invalid input!

# # ## Try 2 ##
# # # Enter Numerator: 2
# # # Enter Denominator: 1
# # # Result is: 2.0
# # # Division is successful.

# # class InputOutString(object):
# #     def __init__(self):
# #         self.s = ""

# #     def getString(self):
# #         self.s = input()
    
# #     def printString(self):
# #         print(self.s.upper())

# # strObj = InputOutString()
# # strObj.getString()
# # strObj.printString()
# # def is_subsequence(s1, s2):
# #     i, j = 0, 0
    
# #     # i pointer s1 ke liye, j pointer s2 ke liye
# #     while i < len(s1) and j < len(s2):
# #         if s1[i] == s2[j]:
# #             i += 1  # Agar match mila toh s1 ka agla character dekho
# #         j += 1      # s2 mein toh hamesha aage badhna hi hai
    
# #     # Agar i s1 ki length tak pahunch gaya, matlab saare characters mil gaye
# #     return i == len(s1)

# # # Example:
# # string1 = "Ragi"
# # string2 = "Roasting Sattu and Grains" # Isme R, a, g, i order mein hain

# # if is_subsequence(string1, string2):
# #     print(f"Yes, '{string1}' is a subsequence!")
# # else:
# #     print("No, it's not.")


# # find all the numbers divisible by 7 but is not a multiple of 5 bw 2000 and 3200 both included
# # l=[]
# # for i in range(2000,3201):
# #     if (i%7==0) & (i%5!=0):
# #         l.append(str(i))
# # print(','.join(l))

# # Factorial of a number
# # def fact(no):
# #     if no ==0 or no==1:
# #         return 1
# #     fact = 1
# #     while no>0:
# #         fact = fact * no
# #         no=no-1
# #     return fact
# # no=int(input())
# # print(fact(no))

# # 3. dict = i : i*i
# # def gendict(n):
# #     d=dict()
# #     for i in range(1,n+1):
# #         d[i]=i*i
# #     return d
# # n=int(input())
# # print(gendict(n))

# # sequence of coma seperated and generate a tuple
# # values=input()
# # l=values.split(",")
# # t=tuple(l)
# # print(l)
# # print(t)

# # Define a class which has at least two methods: 
# # getString: to get a string from console input 
# # printString: to print the string in upper case. 
# # Also please include simple test function to test the class methods.

# # class InputOutString:
# #     def __init__(self):
# #         self.text=""
# #     def getString(self):
# #         self.text=input()
# #     def printString(self):
# #         print(self.text.upper())
# # def test():
# #     strObj = InputOutString()
# #     strObj.getString()
# #     strObj.printString()
# # test()

# # LEVEL - 2

# # WAP that calclates and prints the value according to the given formula
# # Q = sqrt[(2*C*D)/H] c & H = 50
# # import math
# # def sqrt(no):
# #     C=50
# #     H=30
# #     val=no.split(',')
# #     res=[]
# #     for i in val:
# #         Q = math.sqrt((2*C*int(i))/H)
# #         res.append(str(round(Q)))

# #     return ",".join(res)
# # no=input()
# # print(sqrt(no))

# # Q2. WAP which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# # input_str = input()
# # dimensions=[int(x) for x in input_str.split(',')]
# # rowNum=dimensions[0]
# # colNum=dimensions[1]
# # multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# # for row in range(rowNum):
# #     for col in range(colNum):
# #         multilist[row][col]= row*col

# # print(multilist)

# #q3. WAP that accepts sequence of lines as ip and prints line after making all characters
# # in the sentence capitalized

# # def uppStr(s):
# #     s1=""
# #     for i in range(len(s)):
# #         s1=s1+s[i].upper()
# #     return s1
# # s=input()
# # print(uppStr(s))

# # Q3. Write a program that accepts a sequence of whitespace separated words as input 
# # and prints the words after removing all duplicate words and sorting them 
# # alphanumerically
# # s = input()
# # words = [word for word in s.split(" ")]
# # print(" ".join(sorted(list(set(words)))))

# # find the maximum sum of any contiguous subarray of size k
# # nums = [2, 1, 5, 1, 3, 2]
# # k = 3

# # window_sum = sum(nums[:k])
# # max_sum = window_sum

# # for i in range(k, len(nums)):
# #     window_sum = window_sum + nums[i] - nums[i - k]
# #     max_sum = max(max_sum, window_sum)

# # print(max_sum)
# # values = []
# # for i in range(1000, 3001):
# #     s = str(i)
# #     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
# #         values.append(s)
# # print(",".join(values))

# # s = input()
# # d={"DIGITS":0, "LETTERS":0}
# # for c in s:
# #     if c.isdigit():
# #         d["DIGITS"]+=1
# #     elif c.isalpha():
# #         d["LETTERS"]+=1
# #     else:
# #         pass
# # print("LETTERS", d["LETTERS"])
# # print("DIGITS", d["DIGITS"])

# # calculate no or digits
# # s = input()
# # d={"DIGITS":0, "LETTERS":0}
# # for c in s:
# #     if c.isdigit():
# #         d["DIGITS"]+=1
# #     elif c.isalpha():
# #         d["LETTERS"]+=1
# #     else:
# #         pass
# # print("LETTERS", d["LETTERS"])
# # print("DIGITS", d["DIGITS"])

# # Write a program that accepts a sentence and calculate 
# # the number of upper case letters and lower case letters.
# # s = input()
# # d={"UPPER CASE":0, "LOWER CASE":0}
# # for c in s:
# #     if c.isupper():
# #         d["UPPER CASE"]+=1
# #     elif c.islower():
# #         d["LOWER CASE"]+=1
# #     else:
# #         pass
# # print("UPPER CASE", d["UPPER CASE"])
# # print("LOWER CASE", d["LOWER CASE"])

# # #Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# # a = input()
# # n1 = int( "%s" % a )
# # n2 = int( "%s%s" % (a,a) )
# # n3 = int( "%s%s%s" % (a,a,a) )
# # n4 = int( "%s%s%s%s" % (a,a,a,a) )
# # print(n1+n2+n3+n4)

# # netAmount = 0
# # while True:
# #     s = input()
# #     if not s:
# #         break
# #     values = s.split(" ")
# #     operation = values[0]
# #     amount = int(values[1])
# #     if operation=="D":
# #         netAmount+=amount
# #     elif operation=="W":
# #         netAmount-=amount
# #     else:
# #         pass
# # print(netAmount)

# # import re
# # value = []
# # items=[x for x in input().split(',')]
# # for p in items:
# #     if len(p)<6 or len(p)>12:
# #         continue
# #     else:
# #         pass
# #     if not re.search("[a-z]",p):
# #         continue
# #     elif not re.search("[0-9]",p):
# #         continue
# #     elif not re.search("[A-Z]",p):
# #         continue
# #     elif not re.search("[$#@]",p):
# #         continue
# #     elif re.search("\s",p):
# #         continue
# #     else:
# #         pass
# #     value.append(p)
# # print(",".join(value))


# from operator import itemgetter


# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))

# print(sorted(l, key=itemgetter(0,1,2)))

# def printDict():
# 	d=dict()
# 	for i in range(1,21):
# 		d[i]=i**2
# 	for (k,v) in d.items():	
# 		print(v)

# printDict()

# class Circle(object):
#     def __init__(self, r):
#         self.radius = r

#     def area(self):
#         return self.radius**2*3.14

# aCircle = Circle(2)
# print (aCircle.area())

# class Rectangle(object):
#     def __init__(self, l, w):
#         self.length = l
#         self.width  = w

#     def area(self):
#         return self.length*self.width

# aRectangle = Rectangle(2,10)
# print(aRectangle.area())

# class Shape(object):
#     def __init__(self):
#         pass

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l

#     def area(self):
#         return self.length*self.length

# aSquare= Square(3)
# print(aSquare.area())

# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1


# n=int(input())
# values = []
# for i in EvenGenerator(n):
#     values.append(str(i))

# print(",".join(values))

# import math
# def bin_search(li, element):
#     bottom = 0
#     top = len(li)-1
#     index = -1
#     while top>=bottom and index==-1:
#         mid = int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index = mid
#         elif li[mid]>element:
#             top = mid-1
#         else:
#             bottom = mid+1

#     return index

# li=[2,5,7,9,11,17,222]
# print(bin_search(li,11))
# print(bin_search(li,12))


# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         lookup_set = set(["a","e","i","o","u","A","E","I","O","U"])

#         idx = []
#         ans = ""
#         for val in s:
#             if val in lookup_set:
#                 idx.append(val)

#         for val in s:
#             if val in lookup_set:
#                 ans += idx.pop()
#             else:
#                 ans += val

#         return ans
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         lookup_set = set(["a","e","i","o","u","A","E","I","O","U"])

#         idx = []
#         ans = ""
#         for val in s:
#             if val in lookup_set:
#                 idx.append(val)

#         for val in s:
#             if val in lookup_set:
#                 ans += idx.pop()
#             else:
#                 ans += val

#         return ans

# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         n = len(nums)

#         prefix = [1] * n
#         postfix = [1] * n

#         # prefix products
#         for i in range(1, n):
#             prefix[i] = prefix[i-1] * nums[i-1]

#         # postfix products
#         for i in range(n-2, -1, -1):
#             postfix[i] = postfix[i+1] * nums[i+1]

#         output = []
#         for i in range(n):
#             output.append(prefix[i] * postfix[i])

#         return output
    

# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         first, second = float(inf), float(inf)
#         for n in nums:
#             if n <= first:
#                 first = n
#             elif n <= second:
#                 second = n
#             else:
#                 return True
#         return False
#         #string compresssion
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         write = 0
#         i = 0

#         while i < len(chars):
#             curr = chars[i]
#             j = i
#             while j < len(chars) and chars[j] == curr:
#                 j += 1 # this index will end at the start of the next group
 
#             chars[write] = curr # overwrite current one
#             write += 1 # next index after i

#             count = j - i # group size
#             if count > 1:
#                 for c in str(count):
#                     chars[write] = c
#                     write += 1 # update position of write pointer. Note that if I move writer by the size of "count", it cannot account for cases like a2b3c -> it will become a2b3bc after this step. At the next iteration, chars[4]=b will be assigned to "c" instead.

#             i = j # move to next group

#         return write
    
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         temp = []

#         for num in nums:
#             if num != 0:
#                 temp.append(num)

#         for i in range(len(temp)):
#             nums[i] = temp[i]

#         for j in range(len(temp), len(nums)):
#             nums[j] = 0
        
#         return nums
        
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         l, r = 0, len(height)-1

#         while l<r:
#             area = (r-l)* min(height[r],height[l])
#             res = max(res, area)

#             if height[l] < height[r]:
#                 l+=1
#             elif height[r] < height[l]:
#                 r-=1
#             else:
#                 l+=1
#         return res
    
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         l, r, count = 0, len(nums) - 1, 0
#         while l < r:
#             total = nums[l] + nums[r]
#             if total == k:
#                 count += 1
#                 l += 1
#                 r -= 1
#             elif total > k:
#                 r -= 1
#             else:
#                 l += 1
#         return count

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         cur_sum = max_k_sum = sum(nums[:k])
#         for i in range(len(nums) - k):
#             cur_sum = -nums[i] + cur_sum + nums[i+k]
#             max_k_sum = max(cur_sum, max_k_sum)
#         return max_k_sum / k
        

# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:

#         # amount in the first k 
#         # store front and back 
#         # go letter by letter 
#         # if letter leaving is vowel -1 
#         # if letter coming in is vowel +1 

#         vowels = {"a","e","i","o","u"}
#         amount = len([character for character in s[:k] if character in vowels]) 
#         first_index = 0
#         max_amount = amount

#         for index,character in enumerate(s[k:]): 

#             if s[first_index] in vowels: 
#                 amount-=1 
            
#             if character in vowels: 
#                 amount+=1

#             first_index+=1

#             if amount > max_amount: 
#                 max_amount = amount

#         return max_amount

# class Solution:
#     def longestSubarray(self, nums):
#         left = zeros = ans = 0
#         for right, v in enumerate(nums):
#             zeros += (v == 0)
#             while zeros > 1:
#                 zeros -= (nums[left] == 0)
#                 left += 1
#             ans = max(ans, right - left)
#         return ans
        

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         l = 0
#         m = 0
        
#         for r in range(len(nums)):
#             if nums[r] == 0:
#                 k -= 1
            
#             while k < 0:
#                 if nums[l] == 0:
#                     k += 1
#                 l += 1
            
#             m = max(m, r - l + 1)
#         return m
        

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         rows = []
#         for i in range(len(grid)):
#             rows.append(grid[i])

#         cols = []
#         for j in range(len(grid)):
#             col = []
#             for i in range(len(grid)):
#                 col.append(grid[i][j])
#             cols.append(col)

#         count = 0
#         for row in rows:
#             for col in cols:
#                 if row == col:
#                     count += 1
        
#         return count


# class Solution:
#     def removeStars(self, s: str) -> str:
#         stack = []
#         for c in s:
#             if stack and c == "*":
#                 stack.pop()
#             else:
#                 stack.append(c)

#         return "".join(stack)
        

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         st=[]
#         for num in asteroids:
#             while st and num < 0 and st[-1]>0:
#                 if st[-1] <-num:
#                     st.pop()
#                     continue
#                 elif st[-1]==-num:
#                     st.pop()
#                 break
#             else:
#                 st.append(num)
#         return st
        

# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         p = 0
#         me = 0
#         for g in gain:
#             me += g
#             p = max(p, me)
#         return p

# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         curr = ""
#         num = 0

#         for ch in s:
#             if ch.isdigit():
#                 num = num * 10 + int(ch)

#             elif ch == "[":
#                 stack.append((curr, num))
#                 curr = ""
#                 num = 0

#             elif ch == "]":
#                 prev, repeat = stack.pop()
#                 curr = prev + curr * repeat

#             else:
#                 curr += ch

#         return curr
    
#     from collections import deque
# class RecentCounter:

#     def __init__(self):
#         self.q = deque()

#     def ping(self, t: int) -> int:
#         self.q.append(t)

#         while self.q[0] < t-3000:
#             self.q.popleft()
        
#         return len(self.q)


# # Your RecentCounter object will be instantiated and called as such:
# # obj = RecentCounter()
# # param_1 = obj.ping(t)



# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         active = deque()
#         spent = deque(senate)

#         while spent:
#             if active and active[0] != spent[0]:
#                 spent.popleft()
#                 spent.append(active.popleft())
#             else:
#                 active.append(spent.popleft())
        
#         return "Radiant" if active[0]=='R' else "Dire"
    
#     from collections import deque
# class RecentCounter:

#     def __init__(self):
#         self.q = deque()

#     def ping(self, t: int) -> int:
#         self.q.append(t)

#         while self.q[0] < t-3000:
#             self.q.popleft()
        
#         return len(self.q)


# # Your RecentCounter object will be instantiated and called as such:
# # obj = RecentCounter()
# # param_1 = obj.ping(t)

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         left_sum = 0
#         right_sum = sum(nums)

#         for index, element in enumerate(nums):
#             right_sum -= element
#             if left_sum == right_sum:
#                 return index
#             left_sum += element
#         return -1        
            
# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         return [list(set(nums1) - set(nums2)),list(set(nums2) - set(nums1))]

#         class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         len1 = len(s)
#         len2 = len(t)
#         i = j = 0
#         while i < len1 and j < len2:
#             if t[j] == s[i]:
#                 i += 1
#             j += 1
#         if i == len1:
#             return True
#         return False

#         class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         temp = []

#         for num in nums:
#             if num != 0:
#                 temp.append(num)

#         for i in range(len(temp)):
#             nums[i] = temp[i]

#         for j in range(len(temp), len(nums)):
#             nums[j] = 0
        
#         return nums

# from collections import deque
# class RecentCounter:

#     def __init__(self):
#         self.q = deque()

#     def ping(self, t: int) -> int:
#         self.q.append(t)

#         while self.q[0] < t-3000:
#             self.q.popleft()
        
#         return len(self.q)
                
# class Solution:
#     def removeStars(self, s: str) -> str:
#         stack = []
#         for c in s:
#             if stack and c == "*":
#                 stack.pop()
#             else:
#                 stack.append(c)

#         return "".join(stack)
        


# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n==0:
#             return True
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n==0:
#                     return True
#         return False

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head
#         while curr:
#             nxt=curr.next   # 先記住下一個
#             curr.next=prev  # 反轉
#             prev=curr       # prev 前進
#             curr=nxt        # curr 前進
#         return prev


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         sums = []
#         c = [0]

#         def _walk(node, targetSum, sums, c):
#             sums.append(0)
#             for i in range(len(sums)):
#                 sums[i] += node.val
#                 if sums[i] == targetSum:
#                     c[0] += 1      
#             if node.left:
#                 _walk(node.left, targetSum, sums.copy(), c)
#             if node.right:
#                 _walk(node.right, targetSum, sums.copy(), c)
        
#         if root:
#             _walk(root, targetSum, sums, c)
        
#         return c[0]

#         class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         rows = []
#         for i in range(len(grid)):
#             rows.append(grid[i])

#         cols = []
#         for j in range(len(grid)):
#             col = []
#             for i in range(len(grid)):
#                 col.append(grid[i][j])
#             cols.append(col)

#         count = 0
#         for row in rows:
#             for col in cols:
#                 if row == col:
#                     count += 1
        
#         return count


# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return None
#         slow, fast = head, head.next.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         slow.next = slow.next.next
#         return head

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 + str2 != str2+str1:
#             return ''
#         gcd = math.gcd(len(str1),len(str2))
#         return str1[:gcd]

    
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         l, r = 0, len(height)-1

#         while l<r:
#             area = (r-l)* min(height[r],height[l])
#             res = max(res, area)

#             if height[l] < height[r]:
#                 l+=1
#             elif height[r] < height[l]:
#                 r-=1
#             else:
#                 l+=1
#         return res

# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         nums = []
#         curr = head
#         while curr:
#             nums.append(curr.val)
#             curr = curr.next
        
#         N = len(nums)
#         res = 0
#         for i in range(N // 2):
#             res = max(res, nums[i] + nums[N - i - 1])
#         return res


from collections import Counter

arr = [2, 3, 4, 2, 3, 5]

freq = Counter(arr)

for num in arr:
    if freq[num] == 1:
        print(num)
        break

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]
        return result

class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = str(num)
        count = len(num_str)

        mapp = {
            1 : "I",
            4 : "IV",
            5 : "V",
            9 : "IX",
            10 : "X",
            40 : "XL",
            50 : "L",
            90 : "XC",
            100 : "C",
            400 : "CD",
            500 : "D",
            900 : "CM",
            1000 : "M"
        }

        roman = ""

        for i in reversed(mapp):
            while num >=i:
                roman += mapp[i] 
                num -= i
        
        return roman

        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1

        while l<r:
            area = (r-l)* min(height[r],height[l])
            res = max(res, area)

            if height[l] < height[r]:
                l+=1
            elif height[r] < height[l]:
                r-=1
            else:
                l+=1
        return res
    
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        if numRows == 1: 
            return s
        cycle_len = 2 * numRows - 2
        
        for i,char in enumerate(s): 
            pos = i % cycle_len 
            if pos < numRows: 
                rows[pos] += char
            else: 
                rows[cycle_len - pos] +=char

        return "".join(rows)