char="*"
row=5
if not(char.endswith(" ")):
    char+=" "
for i in range(row):
    print(" "*i+char*(row-i))
for j in range(1,row+1):
    print(" "*(row-j)+char*j)