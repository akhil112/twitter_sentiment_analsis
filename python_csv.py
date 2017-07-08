import csv


list=[]
file=open('/Users/akhilmaddu/desktop/sample_csv.csv','rb')
reader=csv.DictReader(file)
for row in reader:
    list.append(row)

file.close()
for i in list:
    print i
