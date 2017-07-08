import matplotlib.pyplot as plt

#user_input=input(" enter a file name:  ")

handler=open('text.txt','r')

facebook_count=0
zuck_count=0
harvard_count=0

for i in handler:
    if i.find("Facebook"):
        facebook_count=facebook_count+1

    elif i.find("zuckerberg"):
        zuck_count=zuck_count+1

    elif i.find("Harvard"):
        Harvard_count=Harvard_count+1

mat_list=[facebook_count,zuck_count,harvard_count]
#plt.hist(mat_list)
plt.hist(mat_list, normed=True, bins=33)
plt.ylabel('names');
plt.xlabel('names count')
plt.show()

print(facebook_count)
print(zuck_count)
print(harvard_count)

