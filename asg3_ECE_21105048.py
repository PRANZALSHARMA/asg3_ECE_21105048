#                                                            Question 1

print('           Question1\n')

Str=input("Enter string:\n")

def count(Str):
    if " " not in Str:
        lst1=[]         #list of charecters already catered
        for character in Str:
            if character not in lst1:
                cnt=0       #count of charecter in string
                for i in range(len(Str)):
                    if Str[i]==character:
                        cnt+=1
                    lst1.append(character)
                print('Number of occurence of',character,'is',cnt)
    else:
        lst2=[]        #list of words already catered
        lst= Str.split()
        for word in lst:
            if word not in lst2:
               cnt=0
               for i in range(len(lst)):
                   if lst[i]==word:
                       cnt+=1
                   lst2.append(word)
               print('Number of occurence of',word,'is',cnt)
count(Str)









#                                                          Question 2

print('          Question 2\n')

date=input("Enter date in dd/mm/yyyy format(eg. 3/2/2022): ")
date=date.split("/")
day=int(date[0])
month=int(date[1])
year=int(date[2])

nonLeap=[31,28,31,30,31,30,31,31,30,31,30,31] #Non leap year
leap=[31,29,31,30,31,30,31,31,30,31,30,31] #Leap year

if year in range(1800,2026) and month in range(1,13):
    if year%4==0:
        if (day+1)<=leap[month-1]:
            print('The next date is',day+1,'/',month,'/',year)
        elif day==leap[month-1]:
            if month==12:
                print('The next date is',1,'/',1,'/',year+1)
            else:
                print('The next date is',1,'/',month+1,'/',year)
        else:
            print('The date is invalid')
    else:
        if (day+1)<=nonLeap[month-1]:
            print('The next date is',day+1,'/',month,'/',year)
        elif day==nonLeap[month-1]:
            if month==12:
                print('The next date is',1,'/',1,'/',year+1)
            else:
                print('The next date is',1,'/',month+1,'/',year)
        else:
            print('The date is invalid')
else:
    print("year or month is out of range")








#                           Questions 3
print("                     Question 3\n")
n=int(input('Number of elements: '))
lst=[]

for i in range(n):
    element=int(input("enter the element: "))
    lst.append(element)

newlst=[]
for i in range(n):
    newlst.append((lst[i],lst[i]**2))
print(newlst)









#                              Question 4
print("                     Question 4\n")

grade=int(input("Enter Grade: "))

if grade==10:
    print("Your grade is A+ and Outstanding Performance.")
elif grade==9:
    print("Your grade is A and Excellent Performance.")
elif grade==8:
    print("Your grade is B+ and Very Good Performance.")
elif grade==7:
    print("Your grade is B and Good Performance.")
elif grade==6:
    print("Your grade is C+ and Average Performance.")
elif grade==5:
    print("Your grade is C and Below Average Performance.")
elif grade==4:
    print("Your grade is D and Poor Performance.")
else:
    print("Enter a valid grade (b/w 4-10)")









#                            Question 5
print("                      Question 5\n")

Str='ABCDEFGHIJK'

for i in range(6):
    print(Str)
    Str=" "+Str[0:len(Str)-2] # Add whitespace in begining and remove last two elements









#                            Question 6
print('                      Question 6\n')
dictionary={}
condition="y"
while condition=="y" or condition=="Y":
    name=input("Enter Name: ")
    sid=int(input('Enter SID: '))

    dictionary[sid]=name # Here 'sid' in key and 'name' is its value

    condition=input("Do you want to enter name and SID <y/n>: ")
    if condition=="n" or condition=="N":
        break

# A>>>
print('A. The dictionary is:\n',dictionary)

# B>>>
dictItems=dictionary.items()
dict_sorted=sorted(dictItems)

dictionary=dict(dict_sorted)

print('B. After sorting:\n',dictionary)

# C>>>
SID=int(input('Enter SID: '))
print("C. Name of student with SID",SID,"is: ",dictionary[SID])









#                                        Question 7
print("                                  Question 7")
breakpoint=int(input("Enter the number of elements in fibonacci sequence: "))
fibonacci=[0,1]
counter=1
while counter<=breakpoint-2:
    fibonacci.append(fibonacci[len(fibonacci)-2]+fibonacci[len(fibonacci)-1]) # Appending the sum of last two elements to the sequence
    counter+=1

print("The fibonacci sequence is: ",fibonacci)

sum=0

for i in fibonacci:
    sum+=i

avg=sum/len(fibonacci)

print("The average of the sequence=",avg)









#                                         Question 8
print("                                   Question 8")

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#A>>>
intersection1=Set1.intersection(Set2)
Union=Set1.union(Set2)

newset1=Union.difference(intersection1) #union-intersection gives uncommon elements in Set1 and Set2
print('A.',newset1)

#B>>>
setA=newset1.difference(Set3)
setB=Set3.difference(newset1)

newset2=setA.union(setB)   #Gives uncommon elements in all sets
print('B.',newset2)

#C>>>
# We have to take union of intersection of pairs and subtract intersection of the triplet from it
intersection2=Set2.intersection(Set3)
intersection3=Set1.intersection(Set3)

triple_Intersection=Set3.intersection(intersection1)  #intersection1 is from part A

setC=intersection1.union(intersection2.union(intersection3)) 

newset3=setC.difference(triple_Intersection)

print("C.",newset3)

#D>>>
setD={1,2,3,4,5,6,7,8,9,10}

newset4=setD.difference(Set1) 

print("D.",newset4)

#E>>>
newset5=setD.difference(Union.union(Set3)) #setD is from part D || Union(Set1 union Set2) is from part A

print("E.",newset5)