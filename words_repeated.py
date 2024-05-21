# write a program to display the words that are repeated more than or equal to N times in the text.

#input:
# First input is string
# Second input is integer N  representing value of number of times words occuring in the text 


#output:
# list of words that are repeated more than or equal to N times in the text
# if no word is repeated print "NA" 

#input:
# cat batman latt cat matter cat latt cat batman cat matter
# 3 


str1=input("Enter the string:")
n=int(input("Enter the number:"))

str1=str1.split()
print(str1,"str1")

counts=dict()

for word in str1:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts,"counts") 

word_list=[]
for key in counts:
    if counts[key]>=n:
        word_list.append(key)
if len(word_list)>0:
    print(word_list,"word_list")
else:
    print("NA")                 
