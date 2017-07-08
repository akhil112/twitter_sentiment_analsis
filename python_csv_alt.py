import unicodecsv

list=[]

#ile=open('/Users/akhilmaddu/desktop/sample_csv.csv','rb')
with open('/Users/akhilmaddu/desktop/python_files/udacity/enrollments.csv','rb') as file:
    reader=unicodecsv.DictReader(file)

    for row in reader:
       list.append(row)



for row in range(5):
    print(list[row])



    #alternative way of above code
    # with open('/Users/akhilmaddu/desktop/sample_csv.csv', 'rb') as file:
     #   reader = unicodecsv.DictReader(file)
     #    list=list(reader)
