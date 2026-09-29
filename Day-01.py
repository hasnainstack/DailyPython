#Reverse a string 

text= "Hassnain"
#Method-01:
reverse = ""

for i in text:
    reverse = i + reverse

print(reverse)
#Method-02:
Reverse = text[::-1]

print(Reverse)