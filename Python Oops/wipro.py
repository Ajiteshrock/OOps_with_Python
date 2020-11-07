'''num , n = raw_input("").split(" ")
num = str(num)
ct=0
for i in num:
    if int(i) == int(n):
        ct+=1
    else:
        continue
print ct
'''
ct=0
string = raw_input()
spcl = ['#','@','!','*','^','$','&','%','(',')','?','/','|',',']
for i in string:
    if i in spcl:
        ct+=1
print ct
