from docutils.utils import release_level_abbreviations

# str=a[::-1]
# print(str)
# if a==str:
#     print("String is palindeome")
# else:
#     print("String is not palindrome")
# def palin(a):
#     reverse_chr=""
#     for i in a:
#         reverse_chr= i +reverse_chr
#     return a==reverse_chr
#
# print(palin("acca"))
#
# def largest_no(lst):
#     lag = lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] > lag:
#             lag=lst[i]
#     print(lag)
#
# lst=[14,74,23,141]
# largest_no(lst)

# def fact(n):
#     fac=1
#     for i in range(1, n+1):
#         fac= fac * i
#     return fac
# print(fact(5))


# a,b=0,1
# for i in range(10):
#     print(a," ")
#     a,b=b,a+b

# def rever(a):
#     reverse_chr = ""
#     for i in a:
#         reverse_chr= i + reverse_chr
#     return reverse_chr
# a="sersft"
# print(rever(a))

# n=13
# for i in range(2,n):
#     if n % i == 0:
#         print(f"{n} is not prime")
#         break
# else:
#     print(f"{n} number is prime")

# a="atsescxouv"
# count=0
# for char in range(len(a)):
#     if a[char] in "aeiou":
#         count+=1
#
# print(f"Number of vouwels are {count}")

# a=[10,11,12,14,16,23,99]
# num=23
# for i in range(len(a)):
#     if a[i]== num:
#         print(f"No is found at index {i}")

# a=[1,2,4,5,6,7]
# n=7
# expet_sum=n*(n+1)/2
# sum=0
# for i in range(len(a)):
#     sum = sum+a[i]
#
# actual_sum=expet_sum-sum

# print(actual_sum)


# a=45789
# sum=0
# for i in str(a):
#     sum=sum+int(i)
#
# print(sum)

# a="asfydsedhw"
# b="whdesdfyas"
# a1=[]
# for i in a:
#     a1+=i
#
# print(a1)
#
# b1=[]
# for i in b:
#     b1+=i
#
# print(b1)
#
# if sorted(a1) == sorted(b1):
#     print("Strings are Anagram")
# else:
#     print("Strings are not Anagram")


# a=[11,21,23,"a",15]
# b=[23,11,"90","a"]
#
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             print(a[i])

# a=[11, 21, 23, 11, 12, 21]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
#
# print(unique)


a=[11,21,34,54,36,22,48]
lar = sec_lar= i
a.sort()
for i in a:
    if i > lar:
        lar=a[i]
        sec_lar=lar
    elif lar> i  >sec_lar:
        sec_lar=a[i]

print(sec_lar)