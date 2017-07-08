
handler=open('len_function.py','r')

count=0
space_count=0
for i in handler:
    count=count+1
    if i==" ":
        space_count=space_count+1
    print(i.upper())

print(space_count)
print(count)
